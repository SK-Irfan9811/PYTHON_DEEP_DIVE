a = 10
b = 10
print(a is b, a == b)
a = 10
b = a
print(a is b, a == b)

s1 = 'hello'
s2 = "HELLO".lower()
print(s1 is s2, s1 == s2)

l1 = [1, 2]
l2 = [1, 2]
print(l1 is l2, l1 == l2)

f1 = 12
f2 = 12.0
print(f1 is f2, f1 == f2)

a = 10 + 0j
b = 10
print(a is b, a == b)

# pmm creates shared ref to the None object only once
v = None
u = None
print(id(v), id(u))
