import importlib
import math

print(importlib)
math_module = importlib.import_module("math")
print(id(math_module), id(math))
print(math_module.sqrt(16))
