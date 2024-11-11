import math
from fractions import Fraction

x = Fraction(10, 20)  # automatically reduced
print(x)
y = Fraction(+4, -3)  # negative sign is always assigned to the numerator
print(y)
print(Fraction(0.34534555))

# constructors
a = Fraction(denominator=-200, numerator=24, _normalize=False)
print(a.numerator, a.denominator)

b = Fraction(numerator=1)
print(b)

print(Fraction('10'))
print(Fraction('22/7'))
print(Fraction('0.125'))
print("######   ARITHMETIC OPS   #############")
print(Fraction(10, 2) * Fraction(100, 10000))

###########################################
print(Fraction(math.pi))
print(Fraction(0.125))
print(format(0.3, '.5f'))
print(format(0.3, '.25f'))
##########################################
# constraining denominator
pi = Fraction(math.pi)
print(pi.limit_denominator(99))

print(pi.limit_denominator(9))

