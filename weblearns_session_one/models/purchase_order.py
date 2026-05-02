from  odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    equipment_category_id = fields.Many2one("equipment.category")

    @api.onchange("product_id")
    def onchange_product_for_equipment_category(self):
        for line in self:
            if line.product_id and line.product_id.equipment_category_id:
                line.equipment_category_id = line.product_id.equipment_category_id
            # else:
            #     line.equipment_category_id = None


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_id = fields.Many2one("res.partner", domain=[("company_id","=",False),
                                                        ("supplier_rank",">",0)])
    prd_list_ids = fields.Many2many("product.product", compute="_get_products_from_vendor")

    @api.depends("partner_id")
    def _get_products_from_vendor(self):
        for po in self:
            if po.partner_id and po.partner_id.is_filter_po_products_category and po.partner_id.prd_list_ids:
                po.prd_list_ids = po.partner_id.prd_list_ids
            else:
                po.prd_list_ids = self.env['product.product'].search([("purchase_ok",'=',True)])
