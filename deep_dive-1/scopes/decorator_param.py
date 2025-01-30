def timed(n):
    def decor(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            time_elapsed = 0
            for i in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                time_elapsed += (end - start)
            print("Avg time of {0} is {1:.6f}".format(fn.__name__, (time_elapsed / n)))
            return result

        return inner

    return decor


def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


def fib_with_recur(n):
    return 1 if n < 3 else fib_with_recur(n - 1) + fib_with_recur(n - 2)


@timed(10)
@memorize
def fib(n):
    return fib_with_recur(n)


print(fib(40))
