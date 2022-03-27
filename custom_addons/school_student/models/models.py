# -*- coding: utf-8 -*-
import random
import datetime
from lxml import etree
from odoo import models, fields, api, _, registry, tools as tl
from odoo.exceptions import  UserError


class Partner(models.Model):
    _inherit = "res.partner"

    def hello_hook(self):
        print("hello hook")
        for contact in self.search([]):
            print(contact.display_name)


class student_test_fees(models.Model):
    _name = "student.test.fees"
    _table = "student_fees_testing"

    name = fields.Char("Fees")


class student_test(models.Model):
    _name = "student.test"

    name = fields.Char(string="Test")


class Address(models.Model):
    _name = "address"
    _rec_name = "street"

    street = fields.Char("Street")
    street_one = fields.Char("Street2")
    city = fields.Char("City")
    state = fields.Char("State")
    country = fields.Char("Country")
    zip_code = fields.Char("Zip Code")


class school_student(models.Model):
    _name = 'school.student'
    _inherit = "address"
    _description = 'school_student.school_student'
    # _order = "school_id"
    _order = "student_seq"
    _rec_name = "name"

    roll_number = fields.Char("Roll Number", groups="school.access_student_admin_level_group")
    name = fields.Char(
        default="Sunny Leaone",
        #    required=True
    )

    student_img = fields.Image("Student Image")
    state = fields.Selection([
        ('done', 'Done'),
        ('draft','Draft'),
        ('paid', 'Paid'),
                              ('progress','Progress')

                              ], string="State")
    student_seq = fields.Integer("Student Sequence")
    school_id = fields.Many2one("school.profile", string="School Name",
                                required=True,
                                # Single Multi domain working
                                # domain="[('school_type','=','public'),"
                                #        "('is_virtual_class', '=', True)]"

                                # It won't be work due to wrong value.
                                #domain="[('school_type', '=', 'Public School')]"

                                # Left side sub fields you can access like this way.
                                # domain="[('currency_id.name', '=', 'EUR')]"

                                # Right side sub fields Odoo doesn't support
                                # domain = "[('currency_id', '=', currency_id.id)]"
                                )
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
                                   index=True)
    total_fees = fields.Float(string="Total Fees", default=200)
    ref_id = fields.Reference(selection=[('school.profile', 'School'),
                               ('account.move', 'Invoice')] ,
                              string="Reference Field",
                              default="school.profile,1")
    active = fields.Boolean(string="Active", default=True)
    bdate = fields.Date(string="Date Of Birth", defualt=fields.Date.today())
    student_age = fields.Char(string="Total Age", compute="_get_age_from_student")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Please provide other student name, Given name already exists.'),
        ('total_fees_check', 'check(total_fees>100)', 'minimum 101 amount allow.')
    ]

    def buttonClickEvent(self):

        raise UserError(_("You click this button. Woohooo!"))

    def specialCommand6(self):
        ids = [15, 31, 32]
        self.write({"hobby_list": [(6, 0, ids)]})

    @api.onchange("school_id")
    def _onchange_school_profile(self):
        currency_id = 0
        if self.school_id:
            currency_id = self.school_id.currency_id.id
        return {"domain": {'currency_id':[('id', '=', currency_id)]}}


    @api.model
    def _change_roll_number(self, add_string):
        """This method is used to add roll number to the student profile."""
        for stud in self.search([('roll_number','!=',False)]):
            stud.roll_number = add_string + "STD20" + str(stud.id)

    def wiz_open(self):

        return self.env['ir.actions.act_window']._for_xml_id("school_student.student_fees_update_action")

        # return {'type': 'ir.actions.act_window',
        #         'res_model': 'student.feees.update.wizard',
        #         'view_mode': 'form',
        #         'target': 'new'}

    def custom_button_method(self):
        return {
            'type':'ir.actions.act_url',
            # 'url':'/web#id=2&action=310&model=school.student&view_type=form&cids=1&menu_id=72',
            # 'url':'http://localhost:8069/web#id=2&action=310&model=school.student&view_type=form&cids=1&menu_id=72',
            # 'url':'contactus',
            'url':'https://www.google.com',
            # 'target':'self'
        }
        return "https://www.google.com"
        # self.env.cr.execute("insert into school_student(name, active) values('from button click', True)")
        # self.env.cr.commit()

        # self._cr.execute("insert into school_student(name, active) values('from button click', True)")
        # self._cr.commit()

        # print("Envi...... ",self.env)
        # print("user id...... ",self.env.uid)
        # print("current user...... ",self.env.user)
        # print("Super user?...... ",self.env.su)
        # print("Company...... ",self.env.company)
        # print("Compaies...... ",self.env.companies)
        # print("Lang...... ",self.env.lang)
        # print("Cr...... ",self.env.cr)
        # print("Hello this is custom_button_method called by you....", self)

        # with_env
        # with_context
        # with_user
        # with_company
        # sudo

        
        # self.env['student.test'].sudo().create({'name':'Student Test Demo.....'})

        # new_cr = registry(self.env.cr.dbname).cursor()
        # partner_id = self.env['res.partner'].with_env(self.env(cr=new_cr)).create({"name":" New Env CR Partner."})
        # partner_id.env.cr.commit()

        # self.custom_new_method(random.randint(1,1000))
        # self.custom_method()

        # cli_commands = tl.config.options
        # print(cli_commands)
        # print(cli_commands.get("db_name"))
        # print(cli_commands.get("db_user"))
        # print(cli_commands.get("db_password"))
        # print(cli_commands.get("addons_path"))
        # print(cli_commands.get("dbfilter"))
        # print(cli_commands.get("weblearns"))
        # print(cli_commands.get("weblearns_author"))
        # if tl.config.options.get("weblearns") == "'Tutorials'":
        #     tl.config.options['weblearns'] = "Odoo Tutorial"
        # print(cli_commands.get("weblearns"))
        # print(cli_commands.get("weblearns_author"))
        # print(tl.config.options['weblearns'])


    def custom_new_method(self, total_fees):
        self.total_fees = total_fees

    def custom_method(self):
        try:
            self.ensure_one()
            # print(self.name)
            # print(self.bdate)
            # print(self.school_id.name)
        except ValueError:
            pass

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

        res = super(school_student, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

        if view_type == "form":
            doc = etree.XML(res['arch'])
            name_field = doc.xpath("//field[@name='name']")
            if name_field:
                # Added one label in form view.
                name_field[0].addnext(etree.Element('label', {'string':'Hello this is custom label from fields_view_get method'}))

            #override attribute
            address_field = doc.xpath("//field[@name='school_address']")
            if address_field:
                address_field[0].set("string", "Hello This is School Address.")
                address_field[0].set("nolabel", "0")

            res['arch'] = etree.tostring(doc, encoding='unicode')

        # if view_type == 'tree':
        #     doc = etree.XML(res['arch'])
        #     school_field = doc.xpath("//field[@name='school_id']")
        #     if school_field:
        #         # Added one field in tree view.
        #         school_field[0].addnext(etree.Element('field', {'string':'Total Fees',
        #                                                         'name': 'total_fees'}))
        #     res['arch'] = etree.tostring(doc, encoding='unicode')
        return res


    @api.model
    def default_get(self, field_list=[]):
        # print("field_list ",field_list)
        rtn = super(school_student, self).default_get(field_list)
        # print("Befor Edit ",rtn)
        rtn['student_fees'] = 4000
        # print("return statement ",rtn)
        return rtn

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
                # print (deadlineDate)
                daysLeft = currentDate - deadlineDate
                # print(daysLeft)

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

    @api.model
    def create(self, values):
        print("Student create method vals ", values)
        rtn = super(school_student, self).create(values)
        return rtn

    #No Decorator
    def write(self, values):
        print("Student write method vals ", values)
        rtn = super(school_student, self).write(values)
        return rtn

    # @api.returns('self', lambda value: value.id)
    # def copy(self, default = {}):
    #     #default['active'] = False
    #     default['name'] = "copy ("+self.name+")"
    #     rtn = super(school_student, self).copy(default=default)
    #     rtn.total_fees = 500
    #     return rtn

    # def unlink(self):
    #     print("self statement ",self)
    #     # for stud in self:
    #     #     if stud.total_fees > 0:
    #     #         raise UserError(_("You can't delete this %s student profile"%stud.name))
    #     rtn = super(school_student, self).unlink()
    #     print("Return statement ",rtn)
    #     return rtn


class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id",
                                  string="School List")
    school_number = fields.Char("School Code")

    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     print("Name ",name)
    #     print("Args ",args)
    #     print("operator ",operator)
    #     print("limit ",limit)
    #     if name:
    #         records = self.search(['|','|','|',('name', operator, name), ('email', operator, name),
    #                                ('school_number', operator, name), ('school_type', operator, name)])
    #         return records.name_get()
    #     return super(SchoolProfile, self).name_search(name=name, args=args, operator=operator, limit=limit)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):

        args = args or []
        domain = []
        # print("Name ",name)
        # print("Args ",args)
        # print("operator ",operator)
        # print("limit ",limit)
        # print("name_get_uid ",name_get_uid)
        # if not name_get_uid:
        #     name_get_uid = self.env['res.users'].browse(1)
        if name:
            domain = ['|','|','|',('name', operator, name), ('email', operator, name),
                     ('school_number', operator, name), ('school_type', operator, name)]
        school_ids = self.with_user(name_get_uid).search(domain+args, limit=limit)

        # searchs = self._search(domain+args, limit=limit, access_rights_uid=name_get_uid)
        # print("self...... _search ",searchs)

        # Below or V13
        # return school_ids.with_user(name_get_uid).name_get()

        # V14
        return school_ids.ids

    # @api.model
    # def create(self, vals):
    #     rtn = super(SchoolProfile, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("Student list is empty!"))
    #     return rtn


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")


class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):

        # print("User Env ",self.env)
        # print("User Env ",self.env.user)
        # print("User Env ",self.env.company)
        # print("User Env ",self.env.companies)
        # print("User Env ",self.env.context)
        #
        # print(" partner values ",vals)

        if 'company_id' not in vals:
            vals['company_id'] = self.env.company.id

        return super(Partner, self).create(vals)


class SchoolStudent(models.Model):
    _inherit = 'school.student'

    parent_name = fields.Char("Parent Name")


class Car(models.Model):
    _name = "car"

    name = fields.Char("Car Name")
    price = fields.Float("Cost")


class CarEngine(models.Model):
    _name = "car.engine"
    _inherits = {"car":"car_id"}

    name = fields.Char("Car Engine Name")
    car_id = fields.Many2one("car", string="Car")