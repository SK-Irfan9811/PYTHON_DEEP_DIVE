lst = [1, 2, 3, 4, 5]
a, b = lst[0], lst[1:]
print(a, b)

a, *b = lst
print(a, b)

a, b, c, d, *f = lst
print(a, b, c, d, f)

a, b, *c, d, e = lst
print(a, b, c, d, e)

# using in RHS
a = [1, 2, 3]
b = [4, 5, 6]
print(*a, *b)

p = 1, 2, 3
q = 'SK'
print(*p, *q)

# unpacking dict
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}
*kys, = d1
print(kys)
print(dict(**d1, **d2))
d3 = {'one': 1, 'two': 2, **d1, **d2, 'f': 200}
print(d3)

# nested unpacking
lst = [1, 2, [3, 4]]
a, *b, (c, d) = lst
print(a, b, c, d)

a, *b, (c, d, e, f) = [1, 2, 3, 4, 5, 'SKIJ']
print(a, b, c, d, e, f)

a, *b, (c, *d) = 1, 2, 3, 'python'
print(a, b, c, d)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
# print(s1+s2) #invalid
print({*s1, *s2})

s3 = {5, 6, 7}
s4 = {7, 8, 9}
print({*s1, *s2, *s3, *s4})  # comparitively easy with union capability s1.union(s2,s3,s4)
print(s1.union(s2, s4, s3))

a, *b, (c) = [1, 2, 3, 4, "Python"]
print(a, b, c)
