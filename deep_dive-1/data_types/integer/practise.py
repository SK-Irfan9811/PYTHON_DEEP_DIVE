import math


def floor(a):
    return a // 1


print("#######################################")
print(floor(2))
print(floor(2.45))
print(floor(2.09))
print(floor(-2.09))
print("#######################################")

# negative numbers
print(-10 // 3)  # floor operation
print(10 // -3)  # floor operation
print(-10 // -3)  # floor operation(gets cancelled)
print(10 // 3)  # truncation
print("#######################################")
print(10 / 3)  # normal div
print(-10 / 3)  # normal div
print(10 / -3)  # normal div
print(-10 / -3)  # normal div
print("#######################################")
print(type(10.0 // 2.0))
print(type(10 // -2))

print("#################################################")
# floor and truncation
print(math.floor(2.0))
print(math.floor(-2.45))
print(type(math.floor(-3.00000000000000000000000000001)))  # floats have precision

print(math.trunc(2.45))
print(math.trunc(-2.45))
print(math.floor(-2.45))
print(math.floor(2.45))
print("#################################################")

# modulo op
# the formulae is a=a-b*(a//b)
print(13 % 4)
print(-13 % 4)
print(13 % -4)
print(-13 % -4)
