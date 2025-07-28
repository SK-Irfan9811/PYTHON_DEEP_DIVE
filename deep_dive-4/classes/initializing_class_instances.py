#To check where class attrs and instance attrs are stored and how to verify them.
class Person:
    is_healthy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Irfan", 23)
p2 = Person("Goutham", 24)
print(p1.__dict__, p2.__dict__,"\n",Person.__dict__)
print(type(p1))
print(type("Hello"),type(str))