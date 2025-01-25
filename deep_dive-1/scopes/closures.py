# adders = []
#
#
# def adder(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# for n in range(1, 4):
#     adders.append(adder(n))
#
# print(adders[0].__code__.co_freevars)
# print(adders[0](100))
# print(adders[1](100))
# print(adders[2](100))
import random
from time import perf_counter

# adders = []
# for n in range(1, 4):
#     adders.append(lambda x: x + n)
#     print(adders[n-1].__closure__)

# def a():
#     n = []
#
#     def inner():
#         n.append(2)
#         print(n)
#
#     return inner
#
#
# f = a()
# f()

# class Averager:
#     def __init__(self):
#         self._total = self._counter = 0
#
#     def add(self, number):
#         self._total += number
#         self._counter += 1
#         print(self._total / self._counter)
#
#
# a = Averager()
# a.add(10)
# a.add(20)
# a.add(30)
#
#
# # can also be done with the closures
# def averager():
#     total = 0
#     count = 0
#
#     def inner(num):
#         nonlocal total
#         nonlocal count
#         total += num
#         count += 1
#         print(total / count)
#
#     return inner
#
#
# a = averager()
# a(10)
# a(20)
# a(30)
#
#
# class Timer:
#     def __init__(self):
#         self._start = perf_counter()
#
#     def __call__(self):
#         print(perf_counter() - self._start)
#
#
# t = Timer()
# t()
# t()
# t()
# t()
#
#
# def timer():
#     start = perf_counter()
#
#     def inner():
#         print(perf_counter() - start)
#
#     return inner
#
#
# tt = timer()
# tt()
# tt()
# tt()
# tt()

# frequency of a function
# def add(*args):
#     return sum(args)
#
#
# def mul(a, b):
#     return a * b
#
#
# def counter(fn):
#     cnt = 0
#
#     def inner(*args, **kwargs):
#         nonlocal cnt
#         cnt += 1
#         print("{0} has invoked {1} times".format(fn.__name__, cnt))
#         print(fn(*args, **kwargs))
#
#     return inner
#
#
# counter_add = counter(add)
# counter_add(1, 2, 3, 4, 5, 6, )
# counter_add(7, 8, 9, 0)
# counter_add(1, 2, 3)

print(list(map(lambda a, b: a + b, [1, 2], [3, 4])))
print(random.randrange(1,20,2))

print([] or 4) # prints the truth value
print([] and 4) # prints the truth value


a=100
def f():
    print(a)
    a=1000000
f()