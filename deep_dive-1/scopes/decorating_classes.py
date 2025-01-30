# Monkey patching - modify objects at runtime
from datetime import datetime, timezone
from fractions import Fraction


# f = Fraction(2, 4)
# print(f.numerator, f.denominator)
#
# Fraction.speak = "Hello, I'm Fraction class"
# print(f.speak)
# Fraction.speak = lambda self, name: "Hello {},I'm a method from fraction class".format(name)
# print(f.speak("Irfan"))
# Fraction.is_integral = lambda self: self.denominator == 1
# f1 = Fraction(1, 2)
# f2 = Fraction(4, 2)
# print(f1.is_integral())
# print(f2.is_integral())


# def decor(cls):
#     cls.make_sound = lambda self, message: "Hi {0}, {1}".format(self.__class__.__name__, message)
#     return cls
#
#
# Fraction = decor(Fraction)
# f = Fraction(2, 4)
# print(f.make_sound("meoww!!"))
#
#
# class Person:
#     pass
#
#
# Person = decor(Person)
# p = Person()
# print(p.make_sound("bhow!!"))


