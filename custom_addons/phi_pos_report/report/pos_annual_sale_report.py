# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from datetime import timedelta
from functools import partial
from itertools import groupby

import psycopg2
import pytz
import datetime
import re
import datetime as dt
from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero, float_round, float_repr, float_compare, date_utils
from odoo.exceptions import ValidationError, UserError
from odoo.http import request
from odoo.osv.expression import AND
import base64
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class ReportAnnualSaleDetails(models.AbstractModel):
    _name = 'report.phi_pos_report.report_pos_annual_saledetails'
    _description = 'Point of Sale Annual Details'


    @api.model
    def get_sale_details(self, date_report_by_year=False, config_ids=False):
        pos_order = self.env['pos.order']
        orders = pos_order.search([('session_id.config_id', 'in', config_ids)])

        compared_date = datetime.datetime(date_report_by_year, 1, 1)
        orders_this_year = [order for order in orders if
                             (order.date_order.date() >= date_utils.start_of(dt.datetime.strptime(compared_date.strftime("%Y-%m-%d"), "%Y-%m-%d"), "year").date())
                             and (order.date_order.date() <= date_utils.end_of(dt.datetime.strptime(compared_date.strftime("%Y-%m-%d"), "%Y-%m-%d"), "year").date())]
        orders_prev_year = [order for order in orders if
                            (order.date_order.date() >=
                             (date_utils.start_of(dt.datetime.strptime(compared_date.strftime("%Y-%m-%d"), "%Y-%m-%d"),
                                                 "year") + relativedelta(years=-1)).date())
                            and (order.date_order.date() <=
                                 (date_utils.end_of(dt.datetime.strptime(compared_date.strftime("%Y-%m-%d"), "%Y-%m-%d"),
                                                   "year") + relativedelta(years=-1)).date())]

        orders_line_this_year = [line for pos_order in orders_this_year for line in pos_order.lines]
        orders_line_prev_year = [line for pos_order in orders_prev_year for line in pos_order.lines]

        sales_today = sum([line.qty for line in orders_line_this_year])
        sales_prev_year = sum([line.qty for line in orders_line_prev_year])

        categorie_ids = set([line.product_id.categ_id for line in orders_line_this_year])

        categories = [
            {
                'name': categ.name,
                'qty': int(sum([line.qty for line in orders_line_this_year if line.product_id.categ_id.id == categ.id])),
                'amount': sum([line.price_subtotal_incl for line in orders_line_this_year if
                               line.product_id.categ_id.id == categ.id]),
                'amount_last_year': sum([line.price_subtotal_incl for line in orders_line_prev_year if
                                         line.product_id.categ_id.id == categ.id]),
            }
            for categ in categorie_ids
        ]
        for categ in categories:
            categ['variance'] = categ['amount'] - categ['amount_last_year']
            categ['perc_variance'] = (categ['variance'] / categ['amount_last_year']) * 100 if categ[
                'amount_last_year'] else 0
        user_currency = self.env.company.currency_id
        categories_result = {
            'currency_precision': user_currency.decimal_places,
            'qty': sum([categ['qty'] for categ in categories]),
            'amount': sum([categ['amount'] for categ in categories]),
            'amount_last_year': sum([categ['amount_last_year'] for categ in categories]),
            'variance': sum([categ['variance'] for categ in categories]),
            'perc_variance': (sum([categ['variance'] for categ in categories]) / sum([categ['amount_last_year'] for categ in categories])) * 100 if sum([categ['amount_last_year'] for categ in categories]) else 0,
        }

        return {
            'categories': categories,
            'sales_today': int(sales_today),
            'sales_prev_year': int(sales_prev_year),
            'ticket_this_year': len(orders_this_year),
            'ticket_prev_year': len(orders_prev_year),
            'variance_sales': sales_today - sales_prev_year,
            'variance_ticket': len(orders_this_year) - len(orders_prev_year),
            'perc_variance_sales': ((sales_today - sales_prev_year) / sales_prev_year) * 100 if sales_prev_year > 0 else 0,
            'perc_variance_ticket': (len(orders_this_year) - len(orders_prev_year) / len(orders_prev_year)) * 100 if len(
                orders_prev_year) > 0 else 0,
            'categories_result': categories_result,
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})
        configs = self.env['pos.config'].browse(data['config_ids'])
        data.update(self.get_sale_details(data['date_report_by_year'], configs.ids))
        return data
