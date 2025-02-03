from collections.abc import Sequence
from html import escape
from numbers import Integral


def singledispatch(fn):
    registry = dict()
    registry[object] = fn

    def decorated(arg):
        return registry.get(Sequence, registry[object])(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn

        return inner

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorated.register = register
    decorated.dispatch = dispatch
    return decorated


# @singledispatch
# def htmlize(a):
#     return escape(str(a))
#
#
# print(htmlize.registry)
#
#
# @htmlize.register(tuple)
# @htmlize.register(list)
# def html_sequence(arg):
#     li = ('<li>{}</li>'.format(htmlize(item)) for item in arg)
#     return '<ul>\n' + "\n".join(li) + '\n</ul>'
#
#
# @htmlize.register(int)
# def html_int(arg):
#     return "{0}(<i>{1}</i>)".format(arg, str(hex(arg)))
#
#
# print(htmlize.registry)
# print(htmlize.register)
# print(htmlize(100))
# print(htmlize([1, 2, 3]))
# print(htmlize((1, 2, 3)))
# print(htmlize({1, 2, 3}))

# we have a caviet here with our decorater.
"""
the type() always looks for the exact class reference , it won't work with subclasses.
Lets say we registed the Integral and Sequence as functions and when we pass htmlize(100) the type(100) 
is not equal to the Integral type, we should use isinstance() for that where it works with subclasses as well.
"""


@singledispatch
def htmlize_generic(arg):
    return escape(str(arg))


@htmlize_generic.register(Sequence)
def html_sequence(arg):
    li = ('<li>{}</li>'.format(item) for item in arg)
    return '<ul>\n' + "\n".join(li) + '\n</ul>'


# print(htmlize_generic.registry)
print(htmlize_generic([1, 2, 3, 4, 5]))
print(htmlize_generic.dispatch(Sequence))
# isinstance vs type
print(type(10) is Integral)
print(type(10) is int)
print(isinstance(10, Integral))
print(isinstance((10, 20, 30), Sequence))
