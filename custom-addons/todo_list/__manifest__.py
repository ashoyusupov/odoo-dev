
{
    'name': 'Todo Custom',
    'version':'1.0',
    'author': 'Ashoyusupov',
    'website': 'https://www.example.com',
    'summary': 'Management for business',
    'description': """Management for business""",
    'category': 'Services',
    'depends':[

        'base',
        'contacts',
        'portal',
    ],
    'data':[
        'security/ir.model.access.csv',        
        'views/todo_views.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3',
}