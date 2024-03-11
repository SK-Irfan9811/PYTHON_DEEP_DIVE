def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b


my_func(10, 20, 30, 40, 50, )
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)