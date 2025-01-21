def _reduce(fn, sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = fn(result, i)
    return result


print(_reduce(lambda x, y: x if x > y else y, [1, 2, 3, -400, 5, 6, 100]))
print(_reduce(lambda x, y: x if x < y else y, [1, 2, 3, -400, 5, 6, 100]))
print(_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))
print(_reduce(lambda x, y: x - y, [1, 2, 3, 4, 5, 6]))
print(_reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6]))
print(_reduce(lambda x, y: x // y, [1, 2, 3, 4, 5, 6]))

# using python inbuild reduce()
import functools
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))

# initializer parameter(optional)
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2000))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 000))

l = [0, 0, 0, 0, "ok", None, False]
print(any(l))
print(all(l))


# fact using reduce function
def fact(n):
    return n and reduce(lambda a, b: a * b, range(1, n + 1))


print(fact(4))
print(fact(1))
print(fact(0))
