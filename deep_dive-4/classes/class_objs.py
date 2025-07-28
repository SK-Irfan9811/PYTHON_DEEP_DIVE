class Irfan:
    pass


# Note: All the classes are of type "type" and created from the class called type..
# but objects created from our classes are of type "created class type".., not of "type"...
# type is parent type of all the classes...

i = Irfan()
print(i)
print(type(i))
print(type(Irfan()))
print(type(Irfan))

# Let's check with isinstance()
print(isinstance(i, Irfan))
print(isinstance(Irfan, type))
print(isinstance(Irfan(), type))
print(isinstance(i, type))
print(isinstance(Irfan(),object))
print(isinstance(Irfan,object))
print(isinstance(object,type))
