a, b, c = [1, 2, 'hello']
print(a, b, c)
a, b, c = 1, 2, 'hi'
print(a, b, c)
a, b = "SK"
print(a, b)
a, b = 10, 20  # assigning values(pythonic way)
print(a, b)
a, b = b, a
print(a, b)
a, b, c, d = {1, 3, 4, 6}
print(a, b, c, d)
a, b, c = {'p': 1, 'q': 2, 'r': 3}
print(a, b, c)
# unpacking dict
dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = dt
print(a, b, c, d)
a, b, c, d = dt.keys()
print(a, b, c, d)
a, b, c, d = dt.values()
print(a, b, c, d)
a, b, c, d = dt.items()
print(a, b, c, d)
