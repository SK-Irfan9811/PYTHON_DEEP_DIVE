class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class SlotPoint:
    __slots__ = ['x', 'y']

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


# point = Point(2, 3)
# slot_point = SlotPoint(3, 4)
# print(point.__dict__.get('x'))
# print(slot_point.x)

# demo of memory savings on using __slots__
from pympler import asizeof


# p = [Point(n, n + 1) for n in range(100000)]
# print(f'Point: {asizeof.asizeof(p)} bytes')
# p = [SlotPoint(n, n + 1) for n in range(100000)]
# print(f'SlotPoint: {asizeof.asizeof(p)} bytes')


# more secure access to instance variables
# __dict__ allows us to define new attributes on the fly and use them.
# __slots__ restricts us to what is listed in it.

class Book:
    pass


class SlotBook:
    __slots__ = 'title', 'est'


book = Book()
book.title = "EPAM"
print(book.title)


book = SlotBook()
book.title = "TR"
# book.price=1000
# print(book.title)





# __slots__ when inherited
# class SlotBook:
#     __slots__ = ()
#
#
# class Book(SlotBook):
#     pass
#
#
# book = Book()
# book.title = "REUTERS"
# print(book.title)
