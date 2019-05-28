И многое другое
===============

http://pythonz.net/versions/named/3.7/


+ Ощутимое повышение производительности во многих областях.

  * Время старта интерпретатора уменьшилось на **10-30%**
  * Возросла скорость вызова методов (**до 20%** в некоторых случаях) за счёт версионирования словаря
  * Сортировка *timsort* в гомогенных контейнерах ускорена на **40-75%** заменой ``PyObject_RichCompareBool()``

+ `PEP-560 <http://pythonz.net/peps/named/0560/>`_, `PEP-563 <http://pythonz.net/peps/named/0563/>`_ — Ускоренный в 7 раз импорт модуля typing.

+ `PEP-561 <http://pythonz.net/peps/named/0561/>`_ — Дистрибуция подсказок типов

+ `PEP-565 <http://pythonz.net/peps/named/0565/>`_ — Показывать DeprecationWarning в __main__

+ `importlib.resources <https://docs.python.org/3.7/whatsnew/3.7.html#whatsnew37-importlib-resources>`_ для импорта данных из пакетов

+ `PEP-567 <http://pythonz.net/peps/named/0567/>`_ — Новый модуль contextvars для работы с переменными контекста
