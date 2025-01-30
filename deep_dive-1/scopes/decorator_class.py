import time
from functools import wraps


class MyClass:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            time_elapsed = 0
            for i in range(self.n):
                start = time.perf_counter()
                result = fn(*args, **kwargs)
                end = time.perf_counter()
                time_elapsed += (end - start)
            print("Avg time is {:.6f}".format(time_elapsed / self.n))
            return result

        return inner


def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@MyClass(10)
@memorize
def get_fib(n):
    return fib(n)


def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


print(get_fib(30))
