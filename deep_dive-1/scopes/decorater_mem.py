# class Fibo:
#     def __init__(self):
#         self.cache = {1: 1, 2: 1}
#
#     def get_fib(self, n):
#         if n not in self.cache:
#             print("Calculating fib - {}".format(n))
#             self.cache[n] = self.get_fib(n - 1) + self.get_fib(n - 2)
#         return self.cache[n]
#
#
# f = Fibo()
# print(f.get_fib(10))
#
#
# def fibo():
#     cache = {1: 1, 2: 1}
#
#     def get_fib(n):
#         if n not in cache:
#             print("calculating fib - {}".format(n))
#             cache[n] = get_fib(n - 1) + get_fib(n - 2)
#         return cache[n]
#
#     return get_fib
#
#
# ff = fibo()
# ff(10)
from functools import lru_cache


def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            print("calculating {} - {}".format(fn.__name__, n))
            cache[n] = fn(n)
        return cache[n]

    return inner


# @memorize
@lru_cache(maxsize=8)  # 128 by default
def fib(n):
    print("Calculating fib - {}".format(n))
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)


from time import perf_counter

start = perf_counter()
print(fib(8))
print(fib(9))
end = perf_counter()
print("time taken  - {0:.6f}".format(end - start))
