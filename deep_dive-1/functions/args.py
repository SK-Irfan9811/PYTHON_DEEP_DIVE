def fun(a, b, *c):
    print(a, b, c)


fun(1, 2, 3)
fun(1, 2, 3, 5, 6, 7, 8, 'j', {'a': 1})
fun(1, 3)
fun(*[11, 12, 13, 14])  # unpacking arg


def fun(*args, **kwargs):
    print(args, kwargs)


fun(2, 3, 4, 5, a=23, b=34)


def avg(*args):
    count = len(args)
    summ = sum(args)
    return count and summ / count  # short-circuiting


print(avg())
print(avg(-1, 0, 1, 2, 3, 4, 5, -6, -7, -8, 9, -1))


def kw_fun(a, b, *args, d):
    print(a, b, args, d)


kw_fun(1, 2, d=3)
kw_fun(1, 2, 3, 4, d=100)


def funn(*, d):
    print(d)


funn(d=56)


# funn(1, 2, 3, d=90) takes no positional arg and only one kwargs

def funnn(a, b, *, d):
    pass


funnn(1, 2, d=3)


# funnn(1, 2, 3, d=90) is invalid as it only accepts 2 pos and one kw arg,* represents the end of the pos args

def fun1(a, b=2, *args, d):
    print(a, b, args, d)


fun1(1, 20, 30, 40, d=100)  # 'b' always gets overridden due to args


def fun2(a, b=2, *args, d=0, e):
    print(a, b, args, d, e)


fun2(10, 23, 44, 56, 78, 90, 9, e=99)
fun2(10, 23, e=99, d='Hello')
