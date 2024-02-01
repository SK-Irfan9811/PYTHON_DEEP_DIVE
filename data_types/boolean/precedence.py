import string

print(True or True and False)
print((True or True) and False)

# short-Circuiting
# True or Y-->always True
# False and Y-->always False
a = 10
b = 0
if b and a / b > 2:  # b have truth value
    print('a is atleast twice b')

# string module
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(type(string.ascii_uppercase))

name = None
# check if num is a digit,None and empty seq have falsy values
if name and name[0] in string.digits:
    print("name can't start with digits")

# boolean ops
print(1 or 3)
print(None or '' or [] or 4)

# avg of numbers with size n
# n = int(input())
#
#
# def sum(n):
#     s = 0
#     for _ in range(n):
#         s += int(input())
#     return s
#
#
# print(n and sum(n) / n)  # short-circuiting

print(1 or 1 / 0)  # here the 1/0 does not get evaluated
# print(0 or 1 / 0)  # here the 1/0 does get evaluated
# print([] and [])
a = 0
b = 0
print(b and a / b)

# not keyword
print(not 2)
print(not '')
print(not False)
print(not (not 9))

print(1 == 1.01)
print(1 + 1 == 2.0)
print(4 == 4 + 0j)
print(3 < 2 < 1 / 0)  # short-circuited
