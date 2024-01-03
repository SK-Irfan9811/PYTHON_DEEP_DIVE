import sys
import time


def calculate(a):
    for _ in range(100000):
        a ** 2


start = time.perf_counter()
calculate(1000 ** 789)
end = time.perf_counter()
print(end - start)

print(sys.maxsize / (1024 ** 3)) # for GB

