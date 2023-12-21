class A:
    def __init__(self, name):
        self.name = name


A.get_name = lambda self: f"hello {self.name}"
a = A("SK")
print(a.get_name())
