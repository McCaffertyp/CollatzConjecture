import datetime
import math
import random

TWENTY_GROUP_ODDS = [2, 6, 10, 14, 18]
TWENTY_GROUP_EVENS = [4, 8, 12, 16, 20]


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 == 1


def get_20g_num(x: int) -> int:
    num = x % 20
    if num == 0:
        return 20
    else:
        return num


def is_power_of_2(x: int) -> bool:
    return math.log2(x).is_integer()


def is_p2f(x: int) -> bool:
    return is_power_of_2(3 * x + 1)


def get_ran_num(min_num: int, max_num: int, inclusive: bool = True) -> int:
    if inclusive:
        return random.randint(min_num, max_num)
    else:
        return random.randint(min_num, max_num - 1)


def get_current_datetime() -> str:
    time_now = datetime.datetime.now()
    year = time_now.year
    month = time_now.month
    day = time_now.day
    hour = time_now.hour
    if int(hour) < 10:
        hour = "0{0}".format(hour)
    minute = time_now.minute
    if int(minute) < 10:
        minute = "0{0}".format(minute)
    second = time_now.second
    if int(second) < 10:
        second = "0{0}".format(second)

    return "{0}-{1}-{2} {3}:{4}:{5}".format(year, month, day, hour, minute, second)
