# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import datetime


year_dict = {'1': 'a',
             '2': 'b',
             '3': 'c',
             '4': 'd',
             '5': 'e',
             '6': 'f',
             '7': 'g',
             '8': 'h',
             '9': 'i',
             '10': 'j',
             '11': 'k',
             '12': 'l',
             '13': 'm'}

month_dict = {'1': 'a',
              '2': 'b',
              '3': 'c',
              '4': 'd',
              '5': 'e',
              '6': 'f',
              '7': 'g',
              '8': 'h',
              '9': 'i',
              '10': 'j',
              '11': 'k',
              '12': 'l', }


class PosMonthlyRevenue(models.TransientModel):
    _name = 'pos.monthly.revenue.wizard'
    _description = ' Récapitulatif de recettes mensuel'

    def generate_report(self):
        data = {'date_report_by_month': self.order_month, 'date_report_by_year': self.order_year, 'config_ids': self.pos_config_ids.ids}
        return self.env.ref('phi_pos_report.sale_monthly_revenue_report').report_action([], data=data)

    order_month = fields.Selection(string="Mois",
                                   selection=[
                                         ('a', 'Janvier'),
                                         ('b', 'Février'),
                                         ('c', 'Mars'),
                                         ('d', 'Avril'),
                                         ('e', 'Mai'),
                                         ('f', 'Juin'),
                                         ('g', 'Juillet'),
                                         ('h', 'Août'),
                                         ('i', 'Septembre'),
                                         ('j', 'Octobre'),
                                         ('k', 'Novembre'),
                                         ('l', 'Décembre'), ],
                                   required=True,
                                   default=month_dict[str(fields.Date.today().month)])
    order_year = fields.Integer(string="Année", required=True, default=datetime.datetime.now().strftime('%Y'))
    pos_config_ids = fields.Many2many('pos.config', 'pos_monthly_revenue_configs',
                                      default=lambda s: s.env['pos.config'].search([]))

    @api.onchange('order_year')
    def onchange_order_year(self):
        if self.order_year <= 0:
            raise ValidationError("Entrer une année valide !")
