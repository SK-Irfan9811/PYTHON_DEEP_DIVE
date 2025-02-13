# timing.py
from time import perf_counter
from collections import namedtuple

print(f"running timing module - {__name__}")

Timings = namedtuple("Timings", "repeats,elapsed,average")


def timeit(code, repeats=10):
    t_time = 0
    for _ in range(repeats):
        start = perf_counter()
        exec(code)
        end = perf_counter()
        t_time += (end - start)
    return Timings(repeats=repeats, elapsed=t_time, average=t_time / repeats)
