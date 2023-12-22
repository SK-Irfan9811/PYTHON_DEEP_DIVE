import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(freq, container):
    for i in range(freq):
        if 'I' in container:
            pass


start1 = time.perf_counter()
membership_test(10000000, char_list)
end1 = time.perf_counter()

start2 = time.perf_counter()
membership_test(10000000, char_tuple)
end2 = time.perf_counter()

start3 = time.perf_counter()
membership_test(10000000, char_set)
end3 = time.perf_counter()

print(
    "list perf", end1 - start1
    , "\ntuple_perf", end2 - start2
    , "\nset perf", end3 - start3
)
