# the default values in the function definition are defined at the time of execution of code
# not at the time of function call,thus causing issue when dealing with datetime module
import time
from datetime import datetime


# def log_msg(msg, *, dt=datetime.utcnow()):
#     print('{0} logged at {1}'.format(msg, dt))
#
#
# def log_msg_fixed(msg, *, dt=None):
#     dt = dt or datetime.utcnow()
#     print('{0} logged at {1}'.format(msg, dt))
#
#
# log_msg("hello this is ironman")
# time.sleep(2)
# log_msg("hello this is spider-man")
#
# log_msg_fixed("hello this is ironman")
# time.sleep(2)
# log_msg_fixed("hello this is spider-man")


def fun(a, b, lst=[]):
    lst.append(a + b)
    print(lst)


fun(1, 2)  # uses a function scoped list
fun(4, 5)  # uses a function scoped list
fun(1, 2, [])  # new list


def fun_fixed(*args, lst=None):
    lst = lst or []
    lst.append(sum(args))
    print(lst)


fun_fixed(1, 2)  # if nothing is passed, a new list is created
fun_fixed(3, 4)
