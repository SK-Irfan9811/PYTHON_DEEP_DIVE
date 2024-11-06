import string

from timeit import timeit

pythonic = timeit('13%2==1', number=100000000)
semi_pythonic = timeit('13%2', number=100000000)
c_style = timeit('13 & 1', number=100000000)

print(pythonic)
print(semi_pythonic)
print(c_style)

# # inplace op
# a = [1, 2, 3]
# print(id(a))
# a+=[4,5]
# print(a)
# print(id(a))



