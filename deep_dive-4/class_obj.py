class MyClass:
    pass


# MyClass is object because ist has state and behaviour
print(MyClass.__name__)  # state
my_obj = MyClass()  # behaviour
print(type(my_obj))
print(type(MyClass))
print(type(type))

print(isinstance(MyClass, type))
print(isinstance(my_obj, type))
print(isinstance(my_obj, MyClass))
print(isinstance(my_obj, object))

print(type(int))
print(type(str))
print(type(object))
print(help(type))
