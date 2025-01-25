import time


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, *kwargs)
        end = perf_counter()
        _args = [str(item) for item in args]
        _kwargs = ['{0}:{1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = ",".join(_args + _kwargs)
        print('{0}({1}) took {2:.6f} seconds to run'.format(fn.__name__, all_args, end - start))
        return result

    return inner


# fib using recursion

def fib_with_mem(n, cache={}):
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]
    result = fib_with_mem(n - 1) + fib_with_mem(n - 2)
    cache[n] = result
    return result


@timed
def get_fib(n):
    return fib_with_mem(n)


print(get_fib(40))


# with loop
@timed
def fib_with_loop(n):
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a + b

    return b


print(fib_with_loop(40))


# with reduce function
@timed
def fib_with_reduce(n):
    from functools import reduce
    initial = (1, 0)
    return reduce(lambda prev, a: (prev[0] + prev[1], prev[0]), range(n), initial)[1]


print(fib_with_reduce(40))


# logger example
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    @wraps(fn)
    def inner(*args, **kwargs):
        dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0} is called at {1}".format(fn.__name__, dt))
        return result

    return inner


@logged
def f1():
    pass

f1()
time.sleep(2)
@logged
def f2():
    pass




f2()
