# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolStudent(http.Controller):
#     @http.route('/school_student/school_student/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_student/school_student/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_student.listing', {
#             'root': '/school_student/school_student',
#             'objects': http.request.env['school_student.school_student'].search([]),
#         })

#     @http.route('/school_student/school_student/objects/<model("school_student.school_student"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_student.object', {
#             'object': obj
#         })
