{
    'name': 'Product Purchase History',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Track product purchase prices',
    'description': """
        This module adds a last purchase price field to products and tracks the purchase price history.
    """,
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/purchase_price_history_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}