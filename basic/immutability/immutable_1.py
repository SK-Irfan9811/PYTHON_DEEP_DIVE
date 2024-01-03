a = [1, 2]
b = [3, 4]
t = (a, b)
print(id(t))
print(id(t[1][0]), t)
a.append(5)
t[1][0] += 100
b.append(6)
t[0][0] += 300
t[0].append(202)
print(id(t[1][0]), t)
print(id(t))
