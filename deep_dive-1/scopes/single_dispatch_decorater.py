# we have default single dispatch decorater which can tackle the generic types isssue we had encountered
from collections.abc import Sequence
from functools import singledispatch
from html import escape
from numbers import Integral


@singledispatch
def htmlize(arg):
    return escape(str(arg))


@htmlize.register(Integral)
def html_int(arg):
    return "{0}(<i>{1}</i>)".format(arg, str(hex(arg)))


@htmlize.register(str)
def html_str(arg):
    return escape(arg).replace('\n', '<br/>')


@htmlize.register(Sequence)
def html_sequence(arg):
    li = ('<li>{}</li>'.format(htmlize(item)) for item in arg)
    return '<ul>\n' + "\n".join(li) + '\n</ul>'


print(htmlize([1, 2, 3, 4]))
print(htmlize([1, 2, 3, "I'm last"]))

# If python encounters tuple and sequence , it chooses the closest kin to it(tuple)
# though themethod names does not matter here we could use _ for all the register methods, as the python only deals with memory address.
