def fun(*, d, **kwargs):
    print(d, kwargs)


fun(a=2., b=3, d=90)
fun(d='single')


def fun_1(**kwargs):
    print(kwargs)


fun_1()
fun_1(a=2, b='hi')


def fun_2(*args, **kwargs):
    print(args, kwargs)


fun_2()
fun_2(2, 3, 4)
fun_2(2, 3, 4, a=23, b=45)
fun_2(a=23, b=45)


# def fun_3(*,**kwargs):
#     pass
# the above is invalid and least one kwarg must-present between them

def fun_4(a, b=10, *, d, **kwargs):
    print(a, b, d, kwargs)


fun_4(1, d=24, h=89)


def fun_5(a, b, c):
    print("hee")


fun_5(1, 2, c=44)
