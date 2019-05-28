
# Hynek Schlawack 2015
# https://pypi.org/project/attrs/
import attr


@attr.s(slots=True, frozen=True)
class MyClass:

    my_num = attr.ib(
        type=int,
        default=42,
        validator=attr.validators.instance_of(int),
        converter=int,
        metadata={'some_meta': 'yes'},
    )
    my_list = attr.ib(factory=list)

    @my_num.validator
    def check_my_num(self, attr, val):
        if val > 42:
            raise ValueError('my_num is too big')


my_cls = MyClass(1, my_list=[1, 2, 3])

# init, repr, сравнения, hash, и т.д.

attr.asdict(my_cls)

###############################################################################

# 3.6
import typing


@attr.s(auto_attribs=True)
class MyClass:

    my_num: int = 42
    my_list: typing.List[int] = attr.Factory(list)


###############################################################################
