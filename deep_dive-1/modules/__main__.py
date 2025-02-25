# __main__.py
from argparse import ArgumentParser
from time import perf_counter
from collections import namedtuple
import argparse

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


if __name__ == '__main__':
    print("this is for cmd")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code", type=str, help="The code to time")
    parser.add_argument("-r","--repeats", default=10,type=int, help="Frequency of executing the code")
    args = parser.parse_args()
    print(timeit(args.code, args.repeats))
