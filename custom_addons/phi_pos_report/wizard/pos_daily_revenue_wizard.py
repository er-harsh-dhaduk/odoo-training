# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosDailyRevenue(models.TransientModel):
    _name = 'pos.daily.revenue.wizard'
    _description = ' Récapitulatif de recettes journalier'

    def generate_report(self):
        data = {'date_report': self.order_date, 'config_ids': self.pos_config_ids.ids}
        return self.env.ref('phi_pos_report.sale_daily_revenue_report').report_action([], data=data)

    order_date = fields.Date(required=True, default=fields.Date.today, string='Date')
    pos_config_ids = fields.Many2many('pos.config', 'pos_daily_revenue_configs',
                                      default=lambda s: s.env['pos.config'].search([]))


