# -*- coding: utf-8 -*-
{
    'name': "school_extend",

    'summary': """
        School Extend""",

    'description': """
        Extend...
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['school_student'],

    # always loaded
    'data': [
        'views/student_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'pre_init_hook':'your_method_name',
    'post_init_hook':'your_method_name',
    'uninstall_hook':'your_method_name',
    'post_load':'your_method_name',
}
