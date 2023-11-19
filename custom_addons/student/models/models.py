from odoo import fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "School"
    # _rec_name = "id"

    name = fields.Char("School Name")
    student_list = fields.One2many("wb.student", "school_id",
                                   string="Student List")
    password = fields.Char("Password")


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

    def header_open_wiz(self):
        return {
            "name": "Set Default School",
            "res_model": "set.default.school.wiz",
            "view_mode": "form",
            "target": "new",
            "context": {"default_student_ids": self.env.context.get("active_ids")},
            "type": "ir.actions.act_window"
        }

    def weblearns(self):
        # print("Hello Weblearns")
        data = []
        school_detail = self.env['wb.school'].search_read([])
        student_detail = self.search_read([])
        # print(school_detail)
        # print(student_detail)

        data.append({"school_detail": school_detail,
                     "student_detail": student_detail})
        print(data)
        return data
        # self.sql_select_query("select * from wb_student")
        # return True

    def sql_select_query(self, qry):
        self.env.cr.execute(qry)
        data = self.env.cr.fetchall()
        print(data)
        return data

    def sql_crud_query(self, qry):
        self.env.cr.execute(qry)
        self.env.cr.commit()
        return True
