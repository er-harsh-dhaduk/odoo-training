# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class School(models.Model):
    _name = "wb.school"
    _description = "This is school profile."

    school_image = fields.Image("School Image", max_width=128, max_height=128)
    name = fields.Char("Name")
    invoice_id = fields.Many2one("account.move")
    invoice_user_id = fields.Many2one("res.users", related="invoice_id.invoice_user_id", store=True)
    invoice_date = fields.Date(related="invoice_id.invoice_date")
    student_list = fields.One2many("wb.student","school_id", string="Students",
                                   help="This field is used to display related students list for this current school.")
    ref_field_id = fields.Reference(selection=[('wb.school','School'),
                                     ('wb.student','Student'),
                                     ('wb.hobby','Hobby'),
                                     ('sale.order','Sale'),
                                     ('account.move', 'Invoice'),
                                     ('purchase.order', 'Purchase')
                                     ])
    binary_field = fields.Binary(string="Upload File")
    binary_file_name = fields.Char("Binary File Name")
    binary_fields = fields.Many2many("ir.attachment", string="Multi Files Upload")
    my_currency_id = fields.Many2one("res.currency", string="(My Currency)", help="Please select the currency!")
    # currency_id = fields.Many2one("res.currency", "Currency")
    amount = fields.Monetary("Amount", currency_field="my_currency_id")

    def unlink(self):
        print("unlink method call!")
        print(self)
        rtn = super(School, self).unlink()
        print(rtn)
        print("unlink method logic finish!")
        return rtn

    # def create(self, vals):
    #     print(self)
    #     print(vals)
    #     rtn = super(School, self).create(vals)
    #     print(rtn)
    #     return rtn

    # @api.model
    @api.model_create_multi
    # @api.model_create_single
    def create(self, vals):
        print(self)
        print(vals)
        # rtn = super(School, self).create(vals)
        rtn = super().create(vals)
        print(rtn)
        return rtn

    def custom_method(self):
        # print("Custom method clicked!")
        # print(self)

        # search(domain, limit, offset, order)
        # [condition, more conditions]

        # print(self.search([]))
        # print(self.search([], order="id desc"))

        abc = self.env["stock.location"].search([("location_id","child_of",7)])
        print(abc)
        abc = self.env["stock.location"].search([("location_id","parent_of",35)])
        print(abc)

        # abc = self.env["res.partner"].search([("child_ids", "child_of", 26)])
        # print(abc)
        # abc = self.env["res.partner"].search([("child_ids", "parent_of", 26)])
        # print(abc)

        # print(self.search([], limit=5, offset=0))
        # print(self.search([], limit=5, offset=1))
        # print(self.search([], limit=5, offset=5))
        # print(self.env["wb.student"].search([]))
        # print(self.search())

        # print(self.search([("name","ilike","web")]))


        # self.name = "Single Update"
        # self.amount = 50

        # self.update({"name": "Write Update", "amount":40})

        # self.write({"name": "Write Update", "amount":40})

        # records = self.search([], limit=5)
        # print(records)

        # records.write({"name":"mass editing name", "amount":1000})

        # for rec in records:
        #     rec.write({"name": f"{rec.id}", "amount":100})


        pass

    def write(self, vals):
        print("Write method called!")
        print(self)
        print(vals)
        rtn = super(School, self).write(vals)
        print(rtn)
        return rtn

class Student(models.Model):
    _name = "wb.student"
    _description = "This is student profile."

    def delete_records(self):
        print(self)
        school_id = self.env["wb.school"].browse([65,66,67,68, 1])
        for school in school_id:
            if not school.exists():
                raise UserError(f"Recordset is not available! {school}")
                print("Instance or Recordset is not available ",school)
            else:
                print("Instance or Recordset is available ", school)
        # print(school_id)
        # print(school_id.unlink())

    def duplicate_records(self):
        # print(self)
        duplicate_record = self.copy({"joining_date":fields.Datetime.now()})
        # print(duplicate_record)

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        print(self)
        print(default)
        rtn = super(Student, self).copy(default=default)
        print(rtn)
        return rtn

    hobby_list = fields.Many2many("wb.hobby","student_hobby_list_relation","student_id","hobby_id")
    hobby_list_ids = fields.Many2many("wb.hobby", string="Hobbies", help="Select hobby list for this student!",
                                      )
    school_id = fields.Many2one(comodel_name="wb.school", string="Select School",
                                default=7, index=True,
                                help="Please select the school profile.")

    # joining_date = fields.Datetime("Join Date!", copy=False, default="2024-01-01 05:00:00")
    joining_date = fields.Datetime("Join Date!", copy=False)
                                   # default=fields.Datetime.now, help="Please select here jointing date of students.")
    # joining_date = fields.Datetime("Join Date!", copy=False, default=fields.Datetime.now())



    # joining_date = fields.Date("Date", default='2024-12-01')
    # joining_date = fields.Date("Date", default=fields.Date.today())
    # joining_date = fields.Date("Date", default=fields.Date.today)
    # joining_date = fields.Date("Date",
    #                            default=fields.Date.context_today,
    #                            help="Provide here student joining date.",
    #                            copy=False)
    #
    # start_date = fields.Date(default= time.strftime("%Y-01-01"))
    # end_date = fields.Date(default= time.strftime("%Y-12-31"))

    school_data = fields.Json()

    @api.model
    def _get_vip_list(self):
        return [('a','1'),('b','2'),('c','3')]

    student_fees = fields.Float(string="Student Fees", default=3.2, help="Please enter student fees for current year.")
    discount_fees = fields.Float("Discount")
    roll_number = fields.Integer(string="Enrollment Number", default=200, index=True)
    gender = fields.Selection(
        [('female','Female'), ('male','Male'),('1','1')], default="female"
    )
    advance_gender = fields.Selection("_get_advance_geneder_list")
    vip_gender = fields.Selection(_get_vip_list, "VIP Gen")
    combobox = fields.Selection(selection=[('female','Female'), ('male','Male'),('1','1')],
                                string="Combo Box"
                                )
    is_default_demo = fields.Boolean(default=True, required=True)
    is_paid = fields.Boolean("-> Paid?", default=True,
                             help="This field is for this student paid or not the full fees!")
    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2")
    name3 = fields.Char("Name3")
    name4 = fields.Char("Name4")

    student_name = fields.Char("STD", size=5)
    address = fields.Text("Student Address Label", help="Enter here student address.", default="Hello student address.....")

    address_html = fields.Html(string="Address HTML Field",
                               #required=1,
                               #default="<h1>This is default value from backend</h1>",
                               readonly=True, copy=False,
                               help="This field is use for the dynamic html code to render into the student profile.")

    final_fees = fields.Float("Final Fees", compute="_compute_final_fees_cal", store=True)
    final_fees1 = fields.Float("Final Fees 1", compute="_compute_final_fees_cal1")

    compute_address_html = fields.Html(string="Compute Address Field.")

    @api.onchange("address_html")
    def onchange_address_html_field(self):
        for record in self:
            record.compute_address_html = record.address_html

    # @api.onchange("student_fees","discount_fees")
    # @api.depends("student_fees","discount_fees")
    def _compute_final_fees_cal(self):
        for record in self:
            record.final_fees = record.student_fees - record.discount_fees
            # record.final_fees1 = record.student_fees - record.discount_fees

    def _compute_final_fees_cal1(self):
        for record in self:
            record.final_fees1 = record.student_fees - record.discount_fees

    def _get_advance_geneder_list(self):
        return [('male','Male'),
                ('female','Female'),
                ('1','1')]

    def json_data_store(self):
        self.school_data = {"name":self.name, "id":self.id, "fees":self.student_fees, "g":self.gender}


    def custom_method(self):
        print("Clicked!")
        self.json_data_store()
        print(self._get_advance_geneder_list)
        data = [
                {"name":"Weblearns-1-Record"},
                {"name":"Weblearns-2-Record"},
                {"name":"Weblearns-3-Record"},
                {"name":"Weblearns-4-Record"},
                {"name":"Weblearns-5-Record"},
            ]

        print(self.env["wb.school"].create(data))


class Hobby(models.Model):
    _name = "wb.hobby"
    _description = "This is student hobbies."

    name = fields.Char("Name")