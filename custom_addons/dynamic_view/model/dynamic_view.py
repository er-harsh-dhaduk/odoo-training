from odoo import fields, models, api, _, tools


class StudentSchoolDynamicView(models.Model):
    _name = "student.school.dynamic.view"
    _description = "Student and School Dynamic View from Postgres."
    _auto = False

    school_name = fields.Char("School Name")
    school_phone = fields.Char("School Phone")
    school_email = fields.Char("School Email")
    school_type = fields.Selection([('public','Public School'),
                                    ('private', 'Private School')],
                                   string="Type of School",
                                   )
    student_name = fields.Char("Student Name")
    student_rno = fields.Char("Roll Number")
    student_fees = fields.Float(string="Student Fees")
    student_seq = fields.Integer("Student Sequence")


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
        create or replace view {} as (
            select std.id as id, 
            std.roll_number as student_rno, 
            std.name as student_name, 
            std.student_fees as student_fees,
            std.student_seq,
             sp.name as school_name,
             sp.email as school_email,
             sp.phone as school_phone,
             sp.school_type as school_type
             from school_student as std join school_profile as sp on std.school_id=sp.id)
        """.format(self._table))