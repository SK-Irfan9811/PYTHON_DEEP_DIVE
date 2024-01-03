import sys
import time


def compare_using_equals(n):
    a = 'I dont get interned I dont get interned' * 200
    b = 'I dont get interned I dont get interned' * 200
    for _ in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern('I get interned I dont get interned' * 200)
    b = sys.intern('I ge interned I dont get interned' * 200)
    for _ in range(n):
        if a is b:
            pass


start1 = time.perf_counter()
compare_using_equals(100000000)
end1 = time.perf_counter()

start2 = time.perf_counter()
compare_using_interning(100000000)
end2 = time.perf_counter()

print("with equals ={}".format(end1 - start1))
print("with interning ={}".format(end2 - start2))

# output
"""
with equals =33.2261034
with interning =2.386168699999999
"""
