# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import  UserError

class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char()
    school_id = fields.Many2one("school.profile", string="School Name")
    hobby_list = fields.Many2many("hobby", "school_hobby_rel","student_id",
                                  "hobby_id", string="Hobby List",
                                  )
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class",
                                       string="Is Virtual Class", store=True)
    school_address = fields.Text(related="school_id.address",
                                 string="Address",
                                 help="This is school address.")
    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string="Student Fees",
                                   index=True, default=1900.00)
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference(selection=[('school.profile', 'School'),
                               ('account.move', 'Invoice')] ,
                              string="Reference Field",
                              default="school.profile,1")


    def write(self, values):
        rtn = super(school_student, self).write(values)
        if not self.hobby_list:
            raise UserError(_("Please select at least one hobby."))
        return rtn

class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id",
                                  string="School List",

                                  )

    # @api.model
    # def create(self, vals):
    #     rtn = super(SchoolProfile, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("Student list is empty!"))
    #     return rtn


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")