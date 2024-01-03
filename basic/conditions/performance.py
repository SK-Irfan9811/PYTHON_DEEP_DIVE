import string
from timeit import timeit

pythonic = timeit('13%2==1', number=100000000)
semi_pythonic = timeit('13%2', number=100000000)
c_style = timeit('13 & 1', number=100000000)

print(pythonic)
print(semi_pythonic)
print(c_style)
print(chr(10084) * 5)
print(string.ascii_lowercase)
print(chr(10084).join(string.ascii_lowercase))
