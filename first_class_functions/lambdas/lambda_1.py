sqr = lambda x: x ** 2
print(type(sqr))
print(type(sqr(4)))
print((lambda x: x ** 2)(100))


def make(a, fn):
    return fn(a)


print(make(2, lambda x: x * 3))
# no annotations and assignments in lambda exp
# lambda x:x=4,lambda x:x+=2,lambda x:int:x+2 are in valid
# breaking of line is valid
t = lambda x: x + 2 \
              - 10 + 100
print(t(900))

# arguments for lambdas
fun = lambda a, b=10, *args, **kwargs: (a + b,*args)
print(fun(1, 2, 3, 4, 5, 6, 7, z=5, n=9))
