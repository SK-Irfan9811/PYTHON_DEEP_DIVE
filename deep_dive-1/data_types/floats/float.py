import math
from fractions import Fraction

print(float(10))
print(float(10.4))
print(float("10.456"))
print(float(Fraction("-10/2")))
print(0.1)
print(format(0.1, '.25f'))  # 0.1 cannot be repr in bin form exactly
print(format(0.125, '.25f'))  # 0.125 has exact repr in bin form
print(1 + 1 + 1 == 3.00000)
print(0.1 + 0.1 + 0.1 == 0.30000)  # strange right? due to not exact repr in bin form
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))  # no change from previous
print(round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5))  # true
print(math.isclose((0.1 + 0.1 + 0.10), 0.3))
print(math.isclose(0.1000, 0.1001, abs_tol=1e+17))  # more abs_total, lesser the strictness
print(math.isclose(0.1000, 0.1001, rel_tol=1e-4))  # more abs_total, lesser the strictness
print((0.125 + 0.125 + 0.125) == 0.375)
print(math.floor(10.0))
print(math.floor(-10.0))