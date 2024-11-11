def my_func():
    """This function calculates ur age"""
    return 100


help(my_func)
print(my_func.__doc__)


def func_1():
    # this is ignored
    # 'p'
    """see me?"""
    pass
print(func_1.__doc__)
print("abcdef,cdghcd".split("cd",2))