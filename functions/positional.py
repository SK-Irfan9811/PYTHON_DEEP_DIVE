# positional args
def func(a, b, c, d):  # positional parameters
    print("{0},{1},{2},{3}".format(a, b, c, d))


# func(10, 20, 30, 40)  # valid


# func(10, 20, 30)  # invalid
# func(10, 20, 30, 40, 50)  # invalid


# default params
def def_fun(a, b, c=10, d=30):
    print("{0},{1},{2},{3}".format(a, b, c, d))


# def_fun(1, 2)
# def_fun(1, b=10)
# def_fun(a=1, b=10)
# def_fun(a=1,4) #invalid
# def_fun(1, 2, c=300, 45) #invalid
# def_fun(1, 2, 3, 4)


def key_func(a=1, b=2, c=3, d=4):
    print(a, b, c, d)


key_func()
key_func(10)
key_func(10, 20)
key_func(10, 20, 30)
key_func(10, 20, 30, 69)
key_func(11, 12, d=69, c=7)
# key_func(11, 12, c=69, 7)#invalid
