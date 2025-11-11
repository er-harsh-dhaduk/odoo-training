import re
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = "res.partner"

    is_filter_po_products_category = fields.Boolean("Filter Products In PO Based On Category", default=False)
    prd_list_ids = fields.Many2many("product.product")
    vendor_priority = fields.Selection([("low","Low"),
                                        ("medium", "medium"),
                                        ("high", "high"),
                                        ("critical", "critical"),
                                        ("strategic", "strategic"),
                                        ], default="medium")


    @api.constrains("mobile")
    def _check_mobile_number(self):
        for record in self:
            if record.mobile:
                mobile_clean = record.mobile.replace("+","").replace(" ","").replace("-","")
                if not mobile_clean.isdigit() or len(mobile_clean) != 10:
                    raise ValidationError("Mobile number must be exactly 10 digits!")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'mobile' in vals and vals['mobile']:
                vals['mobile'] = self._format_mobile_number(vals['mobile'])
        return super().create(vals_list)

    def write(self, vals_list):
        for vals in vals_list:
            print(vals)
            if 'mobile' in vals and vals_list['mobile']:
                vals_list['mobile'] = self._format_mobile_number(vals_list['mobile'])
        return super().write(vals_list)

    def _format_mobile_number(self, mobile):
        if mobile:
            mobile_data = re.sub(r'[^\d]','', mobile)
            if len(mobile_data) == 10:
                return f"+{mobile_data}"
        return mobile