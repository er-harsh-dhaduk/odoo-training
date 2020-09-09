# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api, _
from odoo.exceptions import  UserError

class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char(default="Sunny Leone")
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
    active = fields.Boolean(string="Active", default=True)
    bdate = fields.Date(string="Date Of Birth", required=True)
    student_age = fields.Char(string="Total Age", compute="_get_age_from_student")

    @api.depends("bdate")
    def _get_age_from_student(self):
        """Age Calculation"""
        today_date = datetime.date.today()
        for stud in self:
            if stud.bdate:
                """
                Get only year.
                """
                # bdate = fields.Datetime.to_datetime(stud.bdate).date()
                # total_age = str(int((today_date - bdate).days / 365))
                # stud.student_age = total_age

                """
                Origin of below source code
                https://gist.github.com/shahri23/1804a3acb7ffb58a1ec8f1eda304af1a
                """
                currentDate = datetime.date.today()

                deadlineDate= fields.Datetime.to_datetime(stud.bdate).date()
                print (deadlineDate)
                daysLeft = currentDate - deadlineDate
                print(daysLeft)

                years = ((daysLeft.total_seconds())/(365.242*24*3600))
                yearsInt=int(years)

                months=(years-yearsInt)*12
                monthsInt=int(months)

                days=(months-monthsInt)*(365.242/12)
                daysInt=int(days)

                hours = (days-daysInt)*24
                hoursInt=int(hours)

                minutes = (hours-hoursInt)*60
                minutesInt=int(minutes)

                seconds = (minutes-minutesInt)*60
                secondsInt =int(seconds)

                stud.student_age = 'You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
                 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt)
            else:
                stud.student_age = "Not Providated...."



    # @api.model_create_multi
    # def create(self, values):
    #     rtn = super(school_student, self).create(values)
    #     return rtn

    # @api.model
    # def create(self, values):
    #     rtn = super(school_student, self).create(values)
    #     return rtn

    #No Decorator
    # def write(self, values):
    #     rtn = super(school_student, self).write(values)
    #     return rtn

    # @api.returns('self', lambda value: value.id)
    # def copy(self, default = {}):
    #     #default['active'] = False
    #     default['name'] = "copy ("+self.name+")"
    #     rtn = super(school_student, self).copy(default=default)
    #     rtn.total_fees = 500
    #     return rtn




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