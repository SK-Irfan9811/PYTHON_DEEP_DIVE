# callable inspace whether an object is callable or not
from _decimal import Decimal

print(callable(print))
print(callable(print()))
print(callable(list))
print(callable(list()))
print(callable(list.append))
print(callable(str.upper))
print(callable("10"))
print(callable(Decimal))
d = Decimal('0.90')
print(callable(d))


class MyClass:
    def __init__(self):
        print("initializing....")


print(callable(MyClass))
a = MyClass()
print(callable(a))


class MyClass_1:
    def __call__(self, *args, **kwargs):
        pass


print(callable(MyClass_1))
aa = MyClass_1()
print(callable(aa))
