from decimal import Decimal
from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_str(arg):
    return html_escape(arg).replace('\n', '<br/>')


def html_list(arg):
    li = ('<li>{}</li>'.format(htmlize(item)) for item in arg)
    return '<ul>\n' + "\n".join(li) + '\n</ul>'


def html_dict(arg):
    li = ('<li>{0}={1}</li>'.format(htmlize(key), htmlize(value)) for key, value in arg.items())
    return '<ul>\n' + "\n".join(li) + '\n</ul>'


def html_int(arg):
    return "{0}(<i>{1}</i>)".format(arg, str(hex(arg)))


def html_real(arg):
    return '{0:.2f}'.format(round(arg, 2))


# print(html_str("""This
#  is Ironman&"""))
# print(html_list([1, 2, 3]))
# print(html_dict({1: "one", 2: "two", 3: "three"}))
# print(html_int(100))


def htmlize(arg):
    registry = {
        int: html_int,
        float: html_real,
        str: html_str,
        dict: html_dict,
        list: html_list,
        tuple: html_list,
        Decimal: html_real,
        object: html_escape
    }
    fn = registry.get(type(arg), registry[object])
    return fn(arg)


# print(htmlize("""This
# is Irfan&&"""))
# print(htmlize(143))
# print(htmlize([1,2,3,4]))
# print(htmlize((1,2,3,4)))
# print(htmlize(({1:2,2:3})))
# print(htmlize(2.3455))
# print(htmlize("&&&&&7"))
# print(htmlize([1,2,[200],"%$$"]))
