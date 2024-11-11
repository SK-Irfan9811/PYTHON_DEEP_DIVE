import sys
import time
from decimal import Decimal

x = 0.1
x_dec = Decimal('0.1')
print(sys.getsizeof(x), sys.getsizeof(x_dec))


def float_unga(n=1):
    for _ in range(n):
        a = 3.145


def decimal_unga(n=1):
    for _ in range(n):
        a = Decimal('3.145')


f_start = time.perf_counter()
float_unga(1000000)
f_end = time.perf_counter()

d_start = time.perf_counter()
decimal_unga(1000000)
d_end = time.perf_counter()

print("float per - {0}\n dec perf - {1}".format(f_end - f_start, d_end - d_start))
