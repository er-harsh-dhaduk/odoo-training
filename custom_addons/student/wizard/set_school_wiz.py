from odoo import api, models, fields


class SetDefaultSchoolWiz(models.TransientModel):
    _name = "set.default.school.wiz"
    _description = "Set default school using wizard"

    name = fields.Many2one("wb.school", string="School")
    student_ids = fields.Many2many("wb.student", string="Students")

    def set_default_school(self):
        self.student_ids.write({"school_id": self.name.id})

    # @api.model
    # def default_get(self, fields_list):
    #     rtn = super().default_get(fields_list)
    #     print(self.env.context.get("active_ids"))
    #     rtn['student_ids'] = self.env["wb.student"].browse(self.env.context.get("active_ids"))
    #     return rtn
