from  odoo import fields, models


class POWiz(models.TransientModel):
    _name = "po.filter.wiz"
    _description = "Purchase Order Filters Based ON Internal Users."

    name = fields.Many2many("res.users", required=True, domain=[('share','=',False)])

    def show_po_orders(self):
        po_list = self.env['purchase.order'].search([("user_id",'in', self.name.ids)])
        return {
            "name":"Procurement Managers :- Purchase Orders",
            "type":"ir.actions.act_window",
            "res_model":"purchase.order",
            "view_mode":"list,form",
            "domain":[("id", 'in', po_list.ids)]
        }