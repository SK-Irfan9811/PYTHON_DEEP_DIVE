import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    while rep:
        fn(*args, **kwargs)
        rep -= 1
    end = time.perf_counter()
    return "time taken - {}".format(end - start)


def compute_powers_1(n, *, start=1, end):
    res = []
    for i in range(start, end + 1):
        res.append(n ** i)
    return res


def compute_powers_2(n, *, start=1, end):
    return [n ** i for i in range(start, end + 1)]


def compute_powers_3(n, *, start=1, end):
    return (n ** i for i in range(start, end + 1))


# print(time_it(print, 1, 2, 3, sep='*', rep=3))
print(time_it(compute_powers_1, 20, end=30, start=1, rep=30000))
print(time_it(compute_powers_2, 20, end=30, start=1, rep=30000))
print(time_it(compute_powers_3, 20, end=30, start=1, rep=30000))
