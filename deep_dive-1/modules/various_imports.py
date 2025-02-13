import sys

for key in sorted(sys.modules):
    print(key)
print("***************************************************")
print("Math module in module's global namespace : ", "math" in globals())
print("Math module in sys.modules : ", "math" in sys.modules)
from math import sqrt

print("Math module in module's global namespace : ", "math" in globals())  # sqrt only added to global namespace
print("Math module in sys.modules : ", "math" in sys.modules)
math_mod = sys.modules["math"]
print(math_mod.pow(2, 3))
print("sqrt module in module's global namespace : ", "sqrt" in globals())
print("sqrt module in sys.modules : ", "sqrt" in sys.modules) # only modules
print(sqrt(100))
print(globals())
