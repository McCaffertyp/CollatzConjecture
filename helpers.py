import math


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 == 1


def is_power_of_2(x: int) -> bool:
    return math.log2(x).is_integer()


def is_p2f(x: int) -> bool:
    return is_power_of_2(3 * x + 1)
