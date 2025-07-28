"""
The result of type(object) and object.__class__ are same but it is safe to use always type() because after all the __class__ attribute is a simple mutable one
"""


# Example
class Jaguar:
    __class__ = "electric"


j = Jaguar()
print(type(j), j.__class__)  # the default value of __class__ is just the class name from where it is instantiated.
print(Jaguar.__dict__)
# the __class__ when used inside a class is treated as a normal attr whereas when we try to do it by monkey patch then it is error because we are
# using predefined attr in the python.
#__class__ is not truly useful to check from which class the passed object is instantiated from, it is sometimes because the default value of __class__
# for every class created is their name itself.