a = [1, 2, 3]
print(id(a))
# a = a + [4]  # changes address
a += [4]  # modify the existing list and so address remains same
print(id(a))

x = 10
y = 10
print(id(x), id(y))
x = 257000009898
y = 257000009898
print(id(x), id(y))
