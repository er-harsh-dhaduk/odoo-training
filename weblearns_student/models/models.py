from odoo import fields, models


class WBStudent(models.Model):
    _name = "wb.student"
    _description = "Student Profile"

    name = fields.Char("Student Name")
    fees = fields.Float("Fees")
    gander = fields.Selection([("male","Male"),("female","Female")], string="Gander")


class AbcDemo(models.Model):
    _name = "abc.demo"
    _description =  "ABC Demo"

    abc = fields.Char("Abc Demo")