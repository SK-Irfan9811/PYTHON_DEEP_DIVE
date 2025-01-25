# decorater

from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)    # this is similar to inner=wraps(fn)(inner)
    def inner(*args, **kwargs):
        """This is decorated"""
        nonlocal count
        count += 1
        print(count)
        fn(*args, *kwargs)

    return inner


@counter
def add(a: int, b: int = 1):
    """Adds up the two numbers
    """
    print(a + b)


# one way to decorate
# add = counter(add)
add(100)
add(100, 300)
add(100, 500)
print(add.__name__, add.__doc__)
