from  odoo import fields, models


class EquipmentCategory(models.Model):
    _name = "equipment.category"
    _description = "Equipment Category"

    name = fields.Char("Name", required=True)
    reference = fields.Char("Reference", required=True)
