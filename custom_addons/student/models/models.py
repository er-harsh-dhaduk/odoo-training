from odoo import fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "School"
    # _rec_name = "id"

    name = fields.Char("School Name")
    student_list = fields.One2many("wb.student","school_id",
                                   string="Student List")


class Student(models.Model):
    _name = "wb.student"
    _description = "Student profile"
    _order = "name desc"

    seq = fields.Integer("Sequence", default=10)
    name = fields.Char("Student Name")
    fees = fields.Integer("Fees")
    school_id = fields.Many2one("wb.school", "School")
    stud_tag_list = fields.Many2many(
        "res.partner.category",
        "student_tag_rel",
        "stud_id",
        "tag_id",
        "Student Tags"
    )

    def weblearns(self):
        print("Hello Weblearns")