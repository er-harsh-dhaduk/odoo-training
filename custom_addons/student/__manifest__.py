# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student',
    'version': '1.2',
    'summary': 'Weblearns',
    'sequence': 10,
    'description': """
Weblearns Tutorial
==================
    """,
    'category': 'Weblearns',
    'website': 'https://www.youtube.com/@Weblearns',
    'depends': ['base', 'mail'],
    'license': 'LGPL-3',
    'data': [
        'data/wb.student.csv',
        'data/record_data.xml',
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'view/view.xml',
        'wizard/set_school_wiz.xml'
    ],
    "assets": {
        "web.assets_backend": [
            "student/static/src/xml/list_controller.xml",
            "student/static/src/js/list_controller.js"
        ]
    }
}
