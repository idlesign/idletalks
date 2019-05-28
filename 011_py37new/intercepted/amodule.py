from typing import Any, List


def __getattr__(name: str) -> Any:
    return lambda *args, **kwargs: print(f'А в модуле {__name__} нет атрибута {name}.')


def __dir__() -> List[str]:
    return ['func_one', 'func_two']


def myfunc():
    print('myfunc called')
