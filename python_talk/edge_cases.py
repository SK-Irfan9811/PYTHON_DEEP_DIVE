import random
import string

from timeit import timeit

# pythonic = timeit('13%2==1', number=100000000)
# semi_pythonic = timeit('13%2', number=100000000)
# c_style = timeit('13 & 1', number=100000000)
#
# print(pythonic)
# print(semi_pythonic)
# print(c_style)

# # inplace op
# a = [1, 2, 3]
# print(id(a))
# a+=[4,5]
# print(a)
# print(id(a))

# a, b, c = 1, 2, 3
# a, b, c = c, a, b = b, a, c = c, b, a
# print(a, b, c)  # right most is evaluated first and every other is assigned from left to right
#
# a = [x, y] = (1, 2)
# print(a, x, y)
#
# [x, y, x] = (1, 2, 3)
# print(x, y)

# {x,y}={1,2} won't work with set as LHS
# print(x,y)

# swap 2 nums
# a, b = 10, 20
# a = a + b
# b = a - b
# a = a - b

# # unpack
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# a, *b = l1
# print(*l2, a, b)
#
# d1 = {'p': 1, 'y': 2}
#
# d2 = {'t': 3, 'h': 4}
#
# d3 = {'h': 5, 'o': 6, 'n': 7}
#
# print({**d1, **d2, **d3})
#
# *q, = "Irfan"  # must be in list or tuple
# [*q] = "SK"  # valid
# # *q = "PP"  # invalid
# print(q)
#
# a, (b, *c), *d = ["a", "Python", "n", "3.4"]
# print(a, b, c, d)
#
# a, *b = (10, 20, 30, 'XYZ', 'Python')
# print(b)
#
#
# def func(*args, a, b=400):
#     pass
#
#
# func(1, 2, 3, a=100)
# # usage of * and / in function definition
# """
# * indicates that after it, all must be keyword only arguments
# / indicates that before it , all must be positional only, no keyword argument
# """
#
#
# def fun(a, b, /, c, d, *, e, f=200):
#     print(a, b, c, d, e, f)
#
#
# fun(10, 20, 30, d=40, e="keyword only")
#
# # b has nothing to do if mentioned before *args
# # def fun(a,b=10,*args,c,d):
# #     pass
# # fun(10,b=100,20,40,70,c=90,d="P")
#
# *b, a = [1, 2, 3, 4, 5]
# print(a, b)
#
#
# # func defaults
# def f(msg, dt="SK"):
#     print(msg + dt)
#
#
# print(f.__defaults__)
# f("hi")
# f("hi",
#   dt="Irfan")  # as we provied the dt value upfront, it won't go and search in function namespace, uses the provided value
# f("hello")

# lambdas
# f = lambda e: d[e]
#
#
# def func():
#     d = {1: 1, 2: 2, 3: 3}
#     f = lambda e: d[e]
#     return sorted(d, key=f)
# func()
# random.seed(1)
# print(random.random(),random.random(),random.random())
a=100
def fun(a=0):
    print(a)
    a=20
fun()