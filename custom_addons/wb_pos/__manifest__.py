# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Weblearns Point Of Sale Development Tutorial',
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

    ],
    'assets': {
        'point_of_sale.assets': [
            "wb_pos/static/src/js/wb_sample_button.js",
            "wb_pos/static/src/xml/wb_sample_button.xml",
            "wb_pos/static/src/js/clearall_button.js",
            "wb_pos/static/src/xml/clearall_button.xml"
        ]
    }
}
