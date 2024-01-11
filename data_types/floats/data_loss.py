import math

print(int(10.01))
print(int(10.0))
print(int(10.500))

print(math.floor(10.0))
print(math.floor(-10.0))
print(math.floor(10.1))
print(math.floor(-10.1))
print(math.floor(-0.01))
print(math.floor(0.01))

print(math.ceil(10.0))
print(math.ceil(-10.0))
print(math.ceil(-10.1))
print(math.ceil(10.1))
print(math.ceil(0.1))
print(math.ceil(-0.1))
print(math.ceil(-0.0))
print(math.ceil(0.0))

print(round(2.34, 0))
print(round(2.51))
print(round(2.34, 1))
print(round(12.34, -1))
print(round(25, -1))
print(round(25.15, 1))
print(round(10.5, 0))
