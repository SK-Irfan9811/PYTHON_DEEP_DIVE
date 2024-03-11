import inspect


def fun():
    pass


class MyClass:
    def func(self):
        pass


print(inspect.isfunction(fun))
print(inspect.ismethod(fun))

print(inspect.isfunction(MyClass().func))
print(inspect.ismethod(MyClass().func))

print(inspect.getsource(fun))
print(inspect.getsource(MyClass().func))
print(inspect.getmodule(MyClass().func))
print(inspect.getmodule(fun))
