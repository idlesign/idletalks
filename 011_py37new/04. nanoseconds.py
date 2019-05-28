# PEP-564: http://pythonz.net/peps/named/0564/

from time import *
# noinspection PyTypeChecker

###############################################################################

# time() -> float [64-bit float, IEEE 754] по прошествии 104 дней при конвертациях начинают терятся наносекунды,
# то есть, уже с мая 1970го теряется точность.
# time_ns() -> int64_t (для представления 1677-2262 гг.)


def measure_times_delta():
    """Замер разрешающей способности.

    Разрешение time_ns() примерно три раза больше по сравнению с time().

    """
    import math

    loops = 10 ** 6

    def measure(func: callable):
        min_dt = [abs(func() - func()) for _ in range(loops)]
        return min(filter(bool, min_dt))

    print('time(): %s' % time())
    print('time_ns(): %s' % time_ns())
    print('time() min delta: %s ns' % math.ceil(measure(time) * 1e9))
    print('time_ns() min delta: %s ns' % measure(time_ns))


# measure_times_delta()

###############################################################################


def print_counters():

    funcs = [
        monotonic_ns,  # monotonic — PEP-418 py3.3
        perf_counter_ns,
        process_time_ns,  # system + user время CPU для всего процесса
    ]

    for func in funcs:
        start = func()
        sleep(0.564)
        print(f'{func.__name__}: {func()-start}')


# print_counters()

###############################################################################

# clock_gettime_ns
# clock_settime_ns(CLOCK_REALTIME, new_time)

def print_clocks():

    for clock_const, clock_id in dict(globals()).items():

        if clock_const.startswith('CLOCK_'):
            print(f'{clock_const}: {clock_gettime_ns(clock_id)}')


print_clocks()

###############################################################################
