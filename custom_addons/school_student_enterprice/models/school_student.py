from odoo import api, fields, models


class SchoolStudent(models.Model):
    _inherit = "school.student"

    start_date = fields.Date("Join Date")
    end_date = fields.Date("End Date")