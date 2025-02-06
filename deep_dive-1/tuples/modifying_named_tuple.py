from collections import namedtuple

Stock = namedtuple("Stock", "name symbol high low")
epam = Stock("EPAM Systems INC", "epm", 200, 50)
print(epam)
epam = Stock(epam.name, epam.symbol, epam.high, 20)
print(epam)
# caviet is that it is painful to code when fields are too many
# we can solve this by slicing and unpacking
thomson = Stock("thomson reuters", "TR", 100, 10)
print(thomson)
# *current, _ = thomson
current = thomson[:3]
print(current)
thomson = Stock(*current, 5)
print(thomson)

# unpacking does not work in modifying middle values
infosys = Stock("Infosys", "INFS", 400, 200)
# *pre, _, *post = infosys ambiguous and error statement
print(infosys)
# let's try with slicing
new_infosys = infosys[:1] + ("INF",) + infosys[2:]
infosys = Stock(*new_infosys)
print(infosys)

# _replace method

Person = namedtuple("Person", "name project exp code rm dm")
irfan = Person("Irfan Shaik", "TR", "1.5y", "TRI-RCIT", "SJ", "AK")
print(irfan)
irfan = irfan._replace(code="TRI-DANA", rm="XX", dm="XXX")
print(irfan)

# extending a namedtuple
Student = namedtuple("Student", "name age cls section rank")
s1 = Student("Irfan", 23, 9, "D", 9)
print(s1)
new_values = Student._fields + ("active",)
Student_new = namedtuple("Student_new", new_values)
s1_new = Student_new(*s1, "yes")
s2 = Student_new._make((s1 + ("No",)))
print(s1_new, s2)

# docs for namedtuples
Car = namedtuple("Car", "brand model drive mileage top_speed")
bmw = Car("BMW", "2025", "rwd", "12", "250")
print(Car.__doc__, Car.model.__doc__)
Car.__doc__ = "Info about luxurious cars"
Car.top_speed.__doc__ = "Top speed attained by the so far"
print(Car.__doc__, bmw.__doc__)

# for default values in namedtuple we can use prototype and __default__ property
# -----> prototype
Vector2D = namedtuple("Vector2D", "a b c d e f g h")
vector1 = Vector2D(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
print(vector1)
vector2 = vector1._replace(a=100, g=300, h=500)
print(vector2)

# ------> __defaults__ property
Vector3D = namedtuple("Vector3D", "a b c d e f g h")
Vector3D.__new__.__defaults__ = (0, 0, 0, 10)
vector3 = Vector3D(1, 2, 3, 4)
print(vector3)
