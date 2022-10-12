{
    'name': 'Test Website',
    'version': '12.0',
    'author': 'Jagruti Patel',
    'category': 'website',
    'sequence' : 1,
    'depends': ['base','website'],
    'data': [
        
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/doctors_details.xml',
        'views/template.xml',
            ],
            
    'description': """
        Website forms

    """,
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
