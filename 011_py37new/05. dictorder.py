
# Сохранение словарём порядка вставки элементов официально закреплено в спецификации языка.
# https://mail.python.org/pipermail/python-dev/2017-December/151283.html

from pprint import pprint


def print_dict(dict_: dict):

    print('===' * 20)

    for key, value in dict_.items():
        print(f'{key}: {value}')

    print('===' * 20)

###############################################################################


# Компактные словари в 3.6
# http://pythonz.net/articles/73/

my_dict = {
    'python': 'value1',
    'schema': 'value2',
    'c++': 'value3',
}

dict_classic = {
    'items_count': 3,
    'items': [
        # (hash, key, value)
        ('--', '--', '--'),
        (-9095698888683775416, 'python', 'value1'),
        ('--', '--', '--'),
        ('--', '--', '--'),
        ('--', '--', '--'),
        ('--', '--', '--'),
        (-799031295762617234, 'c++', 'value3'),
        (-4226706071475375297, 'schema', 'value2'),
    ]
}

dict_compact = {
    'items_count': 3,
    'items_index': [0, 1, 0, 0, 0, 0, 1, 1],
    'items': [
        (-9095698888683775416, 'python', 'value1'),
        (-4226706071475375297, 'schema', 'value2'),
        (-799031295762617234, 'c++', 'value3'),
    ]
}

# Современные словари в Python: Сочетание дюжины отличных идей
# http://pythonz.net/videos/95/

###############################################################################

mydict = {
    'Первый': 1,
    'Второй': 2,
}

mydict.update({
    'Третий': 3,
    'Четвёртый': 4,
    'Никакой': None,
})

mydict['Пятый'] = 5

# print_dict(mydict)

mydict.pop('Никакой')
del mydict['Второй']

# print_dict(mydict)
#
# pprint(mydict)

###############################################################################


class MyClass:

    b = 1
    a = 2
    c = 3

    def do(self, **kwargs):
        # PEP-468: http://pythonz.net/peps/named/0468/ — Сохранение порядка **kwargs для функций.
        print_dict(kwargs)

# print_dict(MyClass.__dict__)
# MyClass().do(first=1, second=2, third=3)
# MyClass().do(first=1, third=3, second=2)

###############################################################################
