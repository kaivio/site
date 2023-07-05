
menu = [
    {'title': 'Home', 'action': '/'},
    {'title': 'Archive', 'action': '/archive'},
    {
        'title': 'List',
        'dropdown': True,
        'submenu': [
            {'title':'Item 1', 'action':'/service1'},
            {'title':'Item 2', 'action':'/service2'},
            {'title':'Item 3', 'action':'/service3'}
         ]
     },
     {'title': 'Test', 'action' : '/test'}
]
