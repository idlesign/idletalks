
# PEP-557: http://pythonz.net/peps/named/0557/


from dataclasses import dataclass, field, asdict

from typing import *


@dataclass(frozen=True)
class MyClass:

    my_num: int = 42
    my_list: List[int] = field(default_factory=list)


my_cls = MyClass(1, my_list=[1, 2, 3])
print(asdict(my_cls))


# Без валидаторов, конвертеров, слотов

# Видео по теме:
# http://pythonz.net/videos/114/


###############################################################################
