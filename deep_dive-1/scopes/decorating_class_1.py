from datetime import datetime, timezone
from fractions import Fraction


def info(obj):
    results = ["time : {}".format(datetime.now(timezone.utc)), "classname : {}".format(obj.__class__.__name__),
               "id : {}".format(hex(id(obj)))]
    for k, v in vars(obj).items():
        results.append("{0}:{1}".format(k, v))
    return results


def decor(cls):
    cls.debug = info
    return cls


@decor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "HI {}".format(self.name)


# Person = decor(Person)
p = Person("Irfan", 23)
print(p.debug())


# @decor
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Over speed!!!")
        else:
            self._speed = new_speed


decor(Automobile)
bmw = Automobile("BMW", "M5 competetion", 2025, 200)
print(bmw.debug())
bmw.speed = 199
print(bmw.debug())

f=Fraction(2,4)
print(Fraction.__slots__)
Fraction.a="200"
print(f.a)

