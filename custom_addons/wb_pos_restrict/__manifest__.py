# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Weblearns POS Restriction',
    'version': '1.2',
    'summary': 'Weblearns',
    'sequence': 10,
    'description': """
Weblearns Tutorial
==================
    """,
    'category': 'Weblearns',
    'website': 'https://www.youtube.com/@Weblearns',
    'depends': ['point_of_sale'],
    'license': 'LGPL-3',
    'data': [
        "xml/view.xml"
    ],
    'assets': {
        'point_of_sale.assets': [
            "wb_pos_restrict/static/src/js/wb_sample_button.js",
            "wb_pos_restrict/static/src/xml/wb_sample_button.xml"
        ]
    }
}
