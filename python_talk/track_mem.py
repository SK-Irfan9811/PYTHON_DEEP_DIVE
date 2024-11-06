


# memory profiler
from memory_profiler import profile


@profile
def my_func():
    a = [i for i in range(1000)]
    return a


my_func()
