# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from lxml import etree


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
    amount = fields.Monetary("Amount", currency_field="my_currency_id", default=0)
    student_id = fields.Many2one("wb.student")

    # @api.model
    # def get_view(self, view_id=None, view_type="form", **options):
    #     rtn = super(School, self).get_view(view_id=view_id, view_type=view_type, **options)
    #     if view_type == "form" and "arch" in rtn:
    #         print(self, view_id, view_type, options)
    #         doc = etree.fromstring(rtn["arch"])
    #
    #         # school_field = etree.Element("field", {"name":"student_id"})
    #         # targetd_field = doc.xpath("//field[@name='name']")
    #         # if targetd_field:
    #         #     targetd_field[0].addprevious(school_field)
    #
    #         targetd_field = doc.xpath("//field[@name='name']")
    #         if targetd_field:
    #             targetd_field[0].set("string","School Name!")
    #             targetd_field[0].set("invisible","1")
    #         rtn['arch'] = etree.tostring(doc, encoding="unicode")
    #         print(rtn)
    #     return rtn

    @api.model
    def default_get(self, fields_list):
        print("Default Get Method ",self, fields_list )
        rtn = super(School, self).default_get(fields_list)
        rtn['name'] = "Sunny Leone"
        rtn['amount'] = 20000
        rtn['my_currency_id'] = 1
        # {"name":"Sunny Leone", amount=20000}
        print(rtn)
        return rtn

    # def unlink(self):
    #     print("unlink method call!")
    #     print(self)
    #     rtn = super(School, self).unlink()
    #     print(rtn)
    #     print("unlink method logic finish!")
    #     return rtn

    # def create(self, vals):
    #     print("Main Create Method",self)
    #     print(vals)
    #     rtn = super(School, self).create(vals)
    #     print(rtn)
    #     return rtn

    # @api.model
    # @api.model_create_multi
    # # @api.model_create_single
    # def create(self, vals):
    #     print("Main Create Method",self)
    #     print(vals)
    #     # rtn = super(School, self).create(vals)
    #     rtn = super().create(vals)
    #     print(rtn)
    #     return rtn

    # @api.model
    # def name_create(self, name):
    #     print("Name Create Method ", self, name)
    #     # rtn = super(School, self).name_create(name)
    #     # print(rtn)
    #     rtn = self.create({"name":name})
    #     return rtn.id, rtn.display_name

    def sub_custom_method(self):
        print("Sub custom method!!!!!")
        # Blank or More then one recordset found it will throws ValueError
        # It's only accept single recordset.
        self.ensure_one()
        print(self)
        print(self.name)

    def custom_method(self):
        print("Custom method clicked!")
        print(self)

        print(self.get_metadata())
        for stud in self.env['wb.student'].search([]):
            print(stud,"   ",stud.name,"   ",stud.get_metadata())
        # stud_obj = self.env["wb.student"]
        # print(stud_obj.fields_get(allfields=["id","name","school_id"], attributes=["name","string"]))

        # fields_get(field_list, attributes)


        # student_list = self.env["wb.student"].search([])
        # print(student_list)
        #
        # student_group_list = student_list.grouped(key="gender")
        # print(student_group_list)
        # for ky in student_group_list:
        #     print(ky.name)
        #     for stud in student_group_list[ky]:
        #         print(f"     {stud.name}")
        #
        # for ky in student_group_list:
        #     print(ky)
        #     for stud in student_group_list[ky]:
        #         print(f"     {stud.name}")



        # stud = self.env['wb.student'].search([])
        # print(stud)
        # stud = self.env['wb.student'].search([], order="school_id")
        # print(stud)
        # stud = self.env['wb.student'].search([], order="school_id desc")
        # print(stud)

        # stud_list = stud.sorted(key= lambda stud: stud.school_id.id)
        # print(stud_list)
        # stud_list = stud.sorted(key=lambda stud: stud.school_id.id,reverse=True)
        # print(stud_list)
        # stud_list = stud.sorted(key=lambda stud: stud.id, reverse=True)
        # print(stud_list)

        # student_obj = self.env['wb.student']
        # student_ids = student_obj.search([])
        # print(student_ids)
        #
        # student_fees = []
        # for student in student_ids:
        #     student_fees.append(student.student_fees)
        #
        # student_fees = self.env['wb.student'].search([]).mapped("school_id").mapped("name")
        #
        # print(student_fees)
        # print(sum(student_fees))

        # stud_obj = self.env["wb.student"]
        # students = stud_obj.search([])
        # print(students)
        #
        # student_filtered = stud_obj.search([("name","ilike","ddd")])
        # print(student_filtered)
        #
        # student_filtered = stud_obj.search([("id","in",students.ids),("name", "ilike", "ddd")])
        # print(student_filtered)
        #
        # # stud_obj = self.env["wb.student"]
        # for stud in students:
        #     if "ddd" in str(stud.name):
        #         stud_obj += stud
        # print(stud_obj)
        #
        # stud_obj = students.filtered(lambda stud: "ddd" in str(stud.name))
        # print(stud_obj)



        # search returns list of ids
        # browse convert ids to recordset

        # for school in self.search([]):
        #     school.sub_custom_method()
        #
        # self.search([("id","=",0)]).sub_custom_method()



        # select * from student where school_id=1;
        # search_read(
        #     domain,
        #     fields [id, name, student_id],
        #     offset=101,
        #     limit=100,
        #     order="",
        #     load=None
        # )

        # recordset => json use this method => read
        # search_read => json


        # stud_obj = self.env["wb.student"]
        # stud_list = stud_obj.search_read([("school_id",">",5)],["id","name","school_id"], limit=4, order="school_id desc")
        # print(stud_list)
        # stud_list = stud_obj.search_read([("school_id",">",5)],["id","name","school_id"], limit=4, order="school_id desc", load=None)
        # print(stud_list)


        # self.read_group(domain,
        #                 fields,
        #                 group by,
        #                 offset=
        #                 limit =
        #                 order by = ""
        #                 lazy = True, False
        # )

        # student_group_by_school = self.env["wb.student"].read_group([],
        #                                   ["school_id", "gender"],
        #                                   ["school_id","gender"], lazy=False)
        # for stud in student_group_by_school:
        #     print(stud)
        # sale_obj = self.env['sale.order.line']
        # total_sales_based_on_state = sale_obj.read_group([("order_id.state","=","sale")],
        #                                                  ["product_id","product_uom_qty:avg"],
        #                                                  ["product_id"])
        # for sale in total_sales_based_on_state:
        #     print(sale)


        # sum, avg, day, month, count
        # print(self.read())
        # abc = self.env["wb.student"].search([])
        # print(abc.read(fields=["name","school_id"], load=None))
        # print(abc)
        # Its return integer value.
        # print(self.env['wb.student'].search([]))
        # len(self.env['wb.student'].search([]))
        # total_records = self.env['wb.student'].search_count([])
        # print(total_records)
        # select id,name from student where id > 100


        # search(domain, limit, offset, order)
        # [condition, more conditions]

        # print(self.search([]))
        # print(self.search([], order="id desc"))
        #
        # print(self.search([], limit=5, offset=0))
        # print(self.search([], limit=5, offset=1))
        # print(self.search([], limit=5, offset=5))
        # print(self.env["wb.student"].search([]))
        # print(self.search())

        # [('1','2','3')]
        # [
        #     ('field name', 'condition', 'field value'),
        #     ('field name', 'condition', 'field value'),
        #     ('field name', 'condition', 'field value')
        #  ]

        # select * from school where amount > 1000;

        # =
        #select * from school where amount = 1000;

        # records = self.search([("amount","=",100)])
        # self.print_table(records)
        # records = self.search([("name","=","Web")])
        # self.print_table(records)
        # records = self.search([("name","=","web")])
        # self.print_table(records)

        # records = self.search([("amount", "=", False)])
        # self.print_table(records)

        # False / None mark as True :- 100 Specific value = 100
        # records = self.search([("amount", "=?", False)])
        # self.print_table(records)

        # >
        # records = self.search([("amount", ">", -1)])
        # self.print_table(records)

        # >=
        # records = self.search([("amount", ">=", -1)])
        # self.print_table(records)

        # <
        # records = self.search([("amount", "<", 100)])
        # self.print_table(records)

        # <=
        # records = self.search([("amount", "<=", 100)])
        # self.print_table(records)

        # !=
        # records = self.search([("amount", "!=", 100)])
        # records = self.search([("name", "!=", "Web")])
        # self.print_table(records)

        # in
        # ("a","b","c","d"), (1,2,3,4,5,6)
        # records = self.search([("name", "=", "Web"),
        #                        ("name", "=","web"),
        #                         ("name", "=","xyz school")])
        # records = self.search([("name", "in", ("Web","web","xyz school"))])
        # self.print_table(records)

        # not in

        # records = self.search([("name", "!=", "Web"),
        #                        ("name", "!=","web"),
        #                         ("name", "!=","xyz school")])
        # records = self.search([("amount", "not in", (False, 0))])
        # self.print_table(records)

        # like
        # records = self.search([("name", "like", "Web")])
        # self.print_table(records)

        # not like
        # records = self.search([("name", "not like", "web")])
        # self.print_table(records)

        # =like
        # records = self.search([("name", "=like", "%Web%")])
        # self.print_table(records)

        # ilike
        # records = self.search([("name", "ilike", "web")])
        # self.print_table(records)

        # not like
        # records = self.search([("name", "not ilike", "web")])
        # self.print_table(records)

        # =ilike
        # records = self.search([("name", "=ilike", "%Web%")])
        # self.print_table(records)

        # child_of
        # records = self.env["stock.location"].search([("location_id", "child_of", 7)])
        # self.print_locations(records)

        # A 1           Child of top to bottom
        # -> B 6
        # -> C 8
        #     -> D 9
        #         -F 10  Parent Of bottom to top

        # parent_of
        # records = self.env["stock.location"].search([("location_id", "parent_of", 22)])
        # self.print_locations(records)


        # Join Query
        # any
        # amount = 0 or name ilike 'web'
        # records = self.env["wb.student"].search([("school_id", "any", ['|',('amount','=',0),('name','ilike','web')])])
        # self.print_table(records)

        # not any
        # amount = 0 or name ilike 'web'
        # records = self.env["wb.student"].search(
        #     [("school_id", "not any", [('name', 'ilike', 'web')])])
        # self.print_table(records)

        # records = self.search([("name", "ilike", 'web')])
        # self.print_school_table(records)
        #
        # records = self.env["wb.student"].search([("school_id.amount", ">=", -1),("school_id.name", "ilike", 'web')])
        # self.print_table(records)

        # (name = web or phone = 12390 or mobile = 1234)
        # (name != web or phone = 101010)
        # (name = weblearns and phone = 10101010)

        # Logical Operator

        # And condition
        # records = self.env['res.partner'].search(['!',("name", "=", 'Azure Interior'),
        #                                           ("mobile",'=',False)])
        # self.print_table(records)

        # [name is set and (phone is not set or mobile is not set)]

        # records = self.env['res.partner'].search(['&','!',
        #                                           ("email", "!=", False),
        #                                           ("phone", 'ilike', '+1'),
        #                                           ("mobile", '=', False)])
        # self.print_table(records)

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

    def print_table(self, records):
        print(f"Total Record Found :- {len(records)}")
        print("ID           Name                        phone                    mobile                 email")
        for rec in records:
            print(f"{rec.id}        {rec.name}                          {rec.phone}                  {rec.mobile}                   {rec.email}")
        print("")
        print("")

    def print_school_table(self, records):
        print(f"Total Record Found :- {len(records)}")
        print("ID           Name                        Amount")
        for rec in records:
            print(f"{rec.id}        {rec.name}                          {rec.amount}")
        print("")
        print("")

    def print_locations(self, records):
        print(f"Total Record Found :- {len(records)}")
        print("ID           Name                        Parent")
        for rec in records:
            print(f"{rec.id}        {rec.name}                          {rec.location_id.name} / {rec.location_id.id}")
        print("")
        print("")

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

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        print("_name_search")
        print(name, domain, operator, limit, order)
        domain = ["|", ("name",operator, name), ("gender", operator, name)]
        rtn = self._search(domain, limit=limit, order=order)
        print(rtn)
        return rtn

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