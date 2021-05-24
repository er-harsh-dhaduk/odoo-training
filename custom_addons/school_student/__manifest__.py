# -*- coding: utf-8 -*-
{
    'name': "school_student",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'school'],

    # always loaded
    'data': [
        'data/hobby.csv',
        'data/school.profile.csv',
        'data/school.student.csv',
        'data/student_data.xml',
        'security/ir.model.access.csv',
        'wizard/student_fees_udpdate_wizard_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/delete_data.xml',
        'data/student_noupdate_example.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
