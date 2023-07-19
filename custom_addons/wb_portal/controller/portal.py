from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http, _
from odoo.tools import groupby as groupbyelem
from operator import itemgetter


class WeblearnsPortal(CustomerPortal):

    @http.route(["/new/student"], type="http", methods=["POST","GET"], auth="user", website=True)
    def registerStudentProfile(self, **kw):
        school_list = request.env['school.profile'].search([])
        vals = {'schools': school_list, 'page_name': "register_student"}
        if request.httprequest.method == "POST":
            print(kw)
            error_list = []
            if not kw.get("name"):
                error_list.append("Name field is mandatory.")
            if not kw.get("school"):
                error_list.append("School field is mandatory.")
            if not kw.get("school").isdigit():
                error_list.append("Invalid school field.")
            elif not request.env['school.profile'].search([('id','=', int(kw.get("school")))]):
                error_list.append("Invalid school field selected value.")
            elif not error_list:
                request.env['school.student'].create({"name": kw.get("name"),
                                                  "school_id": int(kw.get("school"))})
                success = "Successfully student registered!"
                vals['success_msg'] = success
            else:
                vals['error_list'] = error_list
        else:
            print("GET Method..........")

        return request.render("wb_portal.new_student_form_view_portal", vals)

    def _prepare_home_portal_values(self, counters):
        rtn = super(WeblearnsPortal, self)._prepare_home_portal_values(counters)
        rtn['student_counts'] = request.env['school.student'].search_count([])
        return rtn

    @http.route(['/my/students', '/my/students/page/<int:page>'], type='http', auth="user", website=True)
    def weblearnsStudentListView(self, page=1, sortby='id', search="", search_in="All", groupby="none", **kw):
        if not groupby:
            groupby = 'none'
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

        groupby_list = {
            'none':{'input':'none', 'label':_("None"), "order":1},
            'country_id': {'input': 'country_id', 'label': _("Country"), "order": 1},
            'school_id': {'input': 'school_id', 'label': _("School"), "order": 1},
        }
        student_group_by = groupby_list.get(groupby, {})
        search_domain = search_list[search_in]['domain']
        default_order_by = sorted_list[sortby]['order']
        if groupby in ("school_id", "country_id"):
            student_group_by = student_group_by.get("input")
            default_order_by = student_group_by+","+default_order_by
        else:
            student_group_by = ''
        student_obj = request.env['school.student']
        total_students = student_obj.sudo().search_count(search_domain)
        stud_url = '/my/students'
        page_detail = pager(url=stud_url,
                            total=total_students,
                            page=page,
                            url_args={'sortby':sortby, 'search_in': search_in, 'search':search, 'groupby':groupby},
                            step=10)
        students = student_obj.sudo().search(search_domain, limit=10, order=default_order_by, offset=page_detail['offset'])

        if student_group_by:
            students_group_list = [{student_group_by:k, 'students':student_obj.concat(*g)} for k, g in groupbyelem(students, itemgetter(student_group_by))]
        else:
            students_group_list = [{'students':students}]
        print(students_group_list)
        vals = {
            # 'students':students,
            'group_students':students_group_list,
            'page_name':'students_list_view', 'pager':page_detail,
                'default_url':stud_url,
                'groupby': groupby,
                'sortby':sortby,
                'searchbar_sortings':sorted_list,
                'searchbar_groupby':groupby_list,
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