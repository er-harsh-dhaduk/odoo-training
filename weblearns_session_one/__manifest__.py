# -*- coding: utf-8 -*-
{
    'name': "Weblearns Session One",
    'summary': "This is weblearns first exersice.",

    'description': """
This is weblearns first exersice.
    """,
    'author': "Weblearns",
    'website': "https://www.yourcompany.com",

    'category': 'Odoo Exersice',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'purchase', 'account'],
    'auto_install':False,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/equipment_category_security.xml',
        'views/quipment_category_view.xml',
        'views/product_view.xml',
        'views/purchase_view.xml',
        'views/partner_view.xml',
        'wizard/po_wiz_view.xml',
        'report/purchase_order_template.xml',
        'views/account_view.xml'
    ]
}

