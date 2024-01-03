# changing the behaviour of class dynamically is called monkey patching
class A:
    def __init__(self, name):
        self.name = name


def greet(self):
    return f"hi {self.name} "


A.get_name = lambda self: f"hello {self.name}"
A.greet = greet
a = A("SK")
print(a.get_name())
print(a.name)
print(a.greet())
