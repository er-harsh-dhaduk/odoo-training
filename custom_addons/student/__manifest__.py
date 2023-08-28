# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Student',
    'version' : '1.2',
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
    'data':[
        'data/wb.student.csv',
        'data/record_data.xml',
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'view/view.xml'
    ]
}
