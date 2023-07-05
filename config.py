
menu = [
    {'title': 'Home', 'action': '/'},
    {'title': 'List', 'action': '/list'},
    {
        'title': 'Services',
        'dropdown': True,
        'submenu': [
            {'title':'Service 1', 'action':'/service1'},
            {'title':'Service 2', 'action':'/service2'},
            {'title':'Service 3', 'action':'/service3'}
         ]
     },
     {'title': 'Test', 'action' : '/test'}
]
