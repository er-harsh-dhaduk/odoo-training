# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/studentFees(http.Controller):
#     @http.route('/custom_addons/student_fees/custom_addons/student_fees', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/student_fees/custom_addons/student_fees/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/student_fees.listing', {
#             'root': '/custom_addons/student_fees/custom_addons/student_fees',
#             'objects': http.request.env['custom_addons/student_fees.custom_addons/student_fees'].search([]),
#         })

#     @http.route('/custom_addons/student_fees/custom_addons/student_fees/objects/<model("custom_addons/student_fees.custom_addons/student_fees"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/student_fees.object', {
#             'object': obj
#         })

