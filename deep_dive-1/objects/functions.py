def square(num):
    return num ** 2


f = square
print(f(3))


# function can be passed as args
def cube(sq_fun, num):
    return sq_fun(num) * num


c = cube
print(c(f, 4))


# functions can return another function
def choose(id):
    if id == 1:
        return square
    elif id == 2:
        return cube


k = choose(2)(f, 8)
print(k)

v = choose(1)
print(v(7))
