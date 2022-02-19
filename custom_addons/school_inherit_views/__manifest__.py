# -*- coding: utf-8 -*-
{
    'name': "School Inherit Views",
    'summary': """
        Creating different views inheritance test cases.""",
    'description': """
        Creating different views inheritance test cases.
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'school', 'school_student'],
    # always loaded
    'data': [
        'views/student_extend.xml'
    ],
}
