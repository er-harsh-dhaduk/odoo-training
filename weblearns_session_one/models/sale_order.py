from  odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner", domain=[("company_id","=",False)])
