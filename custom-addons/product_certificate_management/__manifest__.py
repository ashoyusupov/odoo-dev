{
    'name': 'Product Certificate Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Manage product certificates and notifications',
    'description': """
        This module adds a product certificate management system with notifications.
    """,
    'depends': ['product', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_certificate_views.xml',
        'data/cron_data.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}