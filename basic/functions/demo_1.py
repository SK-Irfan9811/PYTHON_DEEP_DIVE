def func_1():
    return func_2()


# func_1() this will raise an error cause func2 is not yet defined.
def func_2():
    return "running function-2"


print(func_1())
