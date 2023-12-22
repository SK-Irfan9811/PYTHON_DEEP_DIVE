t = [1, 2]
try:
    t[0] += 2
except TypeError:
    print(t)
print(t)

a = [100, 200]
b = [300, 400]
tp = (a, b)
a += [5]
print(tp)
