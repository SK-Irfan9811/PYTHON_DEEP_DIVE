class Person:
    is_healthy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Irfan", 23)
p2 = Person("Goutham", 24)
print(p1.__dict__, p2.__dict__,Person.__dict__)
