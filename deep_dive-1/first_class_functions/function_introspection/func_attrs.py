# dir fetches all valid attrs of an object
def fun(a, b=10, c=20, *, kw1, kw2=100, **kwargs):
    pass


print(fun.__name__)
print(fun.__defaults__)
print(fun.__kwdefaults__)
print(fun.__code__)
