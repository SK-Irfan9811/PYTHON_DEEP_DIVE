from functools import partial


def _pow(base, exp):
    return base ** exp


sq = partial(_pow, exp=2)
cube = partial(_pow, exp=3)
print(sq(2))
print(sq(3))
print(sq(4))
print(cube(3))
print(cube(4))
print(cube(5, exp=2))
