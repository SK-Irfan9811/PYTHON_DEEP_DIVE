import decimal
import math
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('-0.1')
print(a + b)

a = Decimal(2)
b = Decimal(4)
print(a + b)

# floor division
print(10 // 3, -10 // 3)
print(Decimal(10) // Decimal(3), Decimal(-10) // Decimal(3))
print(-135 // 4, Decimal(-135) // Decimal(4))

dec_x = Decimal('0.01')
x = 0.01
print(format(math.sqrt(x), '.25f'))
print(format(math.sqrt(dec_x), '.25f'))
print(format(dec_x.sqrt(), '.25f'))

x = -10
y = 3
print(divmod(x, y), x == (y * (x // y)) + (x % y))
x = Decimal(-10)
y = Decimal(3)
print(divmod(x, y), x == y * (x // y) + x % y)

# some other functions
a = Decimal(1.5)
print(a.ln())
print(a.exp())
print(format(a.sqrt(), '.50f'))
