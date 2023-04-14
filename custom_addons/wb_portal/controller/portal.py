from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http, _


class WeblearnsPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn['student_counts'] = request.env['school.student'].search_count([])
        return rtn

    @http.route(['/my/students', '/my/students/page/<int:page>'], type='http', auth="user", website=True)
    def weblearnsStudentListView(self, page=1, sortby='id', search="", search_in="All", **kw):
        print("Hello you called /my/students controller......")
        # based on which field -> search ?
        # what search user is searching -> search value ?
        sorted_list = {
            'id':{'label':'ID Desc', 'order':'id desc'},
            'name':{'label':'Name', 'order':'name'},
            'school_id':{'label':'School', 'order':'school_id'}
        }

        search_list = {
            'All': {'label': 'All', 'input': 'All', 'domain':[]},
            'Name': {'label': 'Student Name', 'input': 'Name', 'domain':[('name','ilike',search)]},
            'School': {'label': 'School', 'input': 'School', 'domain':[('school_id.name','ilike',search)]}
        }

        search_domain = search_list[search_in]['domain']


        default_order_by = sorted_list[sortby]['order']
        student_obj = request.env['school.student']
        total_students = student_obj.sudo().search_count(search_domain)
        page_detail = pager(url='/my/students',
                            total=total_students,
                            page=page,
                            url_args={'sortby':sortby, 'search_in': search_in, 'search':search},
                            step=5)
        students = student_obj.sudo().search(search_domain, limit=5, order=default_order_by, offset=page_detail['offset'])
        vals = {'students':students, 'page_name':'students_list_view', 'pager':page_detail,
                'sortby':sortby,
                'searchbar_sortings':sorted_list,
                'search_in':search_in,
                'searchbar_inputs':search_list,
                'search':search,
                }

        return request.render("wb_portal.wb_students_list_view_portal", vals)

    @http.route(['/my/student/<model("school.student"):student_id>'], auth="user", type='http', website=True)
    def weblearnsStudentFormView(self, student_id, **kw):
        vals = {"student": student_id, 'page_name':'students_form_view'}
        student_records = request.env['school.student'].search([])
        student_ids = student_records.ids
        student_index = student_ids.index(student_id.id)
        if student_index != 0 and student_ids[student_index - 1]:
            vals['prev_record'] = '/my/student/{}'.format(student_ids[student_index-1])
        if student_index < len(student_ids) - 1 and student_ids[student_index+1]:
            vals['next_record'] = '/my/student/{}'.format(student_ids[student_index+1])
        return request.render("wb_portal.wb_students_form_view_portal", vals)

    @http.route("/my/student/print/<model('school.student'):student_id>", auth="user", type="http", website=True)
    def weblearnsStudentReportPrint(self, student_id, **kw):
        print("Hello this is called ",student_id)
        return self._show_report(model=student_id, report_type='pdf',
                                 report_ref='wbcustom_header_foooter_pdf.school_student_profile_report_temp',
                                 download=False)