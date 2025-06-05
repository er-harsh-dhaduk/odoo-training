from odoo import fields, models


class Product(models.Model):
    _inherit = "product.template"

    equipment_category_id = fields.Many2one("equipment.category")
