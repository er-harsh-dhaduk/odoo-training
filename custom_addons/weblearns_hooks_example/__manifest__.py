# -*- coding: utf-8 -*-
{
    'name': "Hooks Examples",
    'summary': """
        Odoo provides 4 types of hooks here is the exampls.""",
    'description': """
        Odoo hooks tutorial
    """,
    'author': "Weblearns",
    'website': "https://www.youtube.com/c/HarshDhaduk/",
    'category': 'Tutorial',
    'version': '0.1',
    'depends': ['contacts'],
    'data': [
    ],
    'pre_init_hook':'_weblearns_pre_init_hook',
    'post_init_hook':'_weblearns_post_init_hook',
    'uninstall_hook':'_weblearns_uninstall_hook',
    'post_load':'_weblearns_post_load_hook'
}
