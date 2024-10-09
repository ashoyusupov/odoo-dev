{
    'name': 'Custom Sale',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Customize Sales module',
    'description': """
        This module extends the functionality of the Sales module.
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}