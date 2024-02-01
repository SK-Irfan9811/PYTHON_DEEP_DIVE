import cmath

c1 = complex(1, 2)
c2 = 1 + 2j
print(c1 == c2, c1 is c2)
print(c1.real, c1.imag, c1.conjugate())
print(c1 + c2)
print(c1 - c2)
print(c1 + 1.0)
print(c1 - 1.0j)
print(c1 * 1.0j)
print(c1 * c2)
print(c1 ** c2)
print(c1 / c2)
# // and % are not supported
a = 4 + 4j
print(cmath.sqrt(a))
