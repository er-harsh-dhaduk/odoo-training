# -*- coding: utf-8 -*-
{
    'name': "Phidias : pos report",

    'summary': "Phidias : pos report",

    'description': "Phidias : pos report",

    'author': "phidias",
    'website': "www.phidias.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '15.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/pos_daily_revenue_wizard.xml',
        'wizard/pos_monthly_revenue_wizard.xml',
        'wizard/pos_annual_revenue_wizard.xml',
        'report/report_pos_daily_saledetails.xml',
        'report/report_pos_monthly_saledetails.xml',
        'report/report_pos_annual_saledetails.xml',
        'views/pos_report.xml',

    ],
    'installable': True,


}
