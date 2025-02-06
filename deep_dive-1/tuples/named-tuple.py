from collections import namedtuple

# disadvantage of changing tuple signature
# person = ("SK", 23)
# last_name, age = person
# print(last_name, age)
# person = ("Irfan", "SK", 23)
# last_name, age = person

# rename
Book = namedtuple("Book", "id,_ssn", rename=True)
b1 = Book(101, 0b100)
print(b1)
print(b1._fields)
print(b1._asdict())
print(type(Book))
print(isinstance(b1, tuple))
book1 = Book(101, 0b100)
book2 = Book(101, 0b100)
print(book1 is book2, book1 == book2)
print(max(book1))