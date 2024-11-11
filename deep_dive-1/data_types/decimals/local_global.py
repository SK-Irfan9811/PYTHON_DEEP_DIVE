# locals and globals
import decimal
from decimal import Decimal

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)

decimal.getcontext().prec = 3
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec += 1
    c = a + b
    print(c)
print(c)
x = Decimal('0.1')
y = Decimal('0.1')
print(x == y, x is y)

a = 1.2
b = 1.20
print(a is b)

for i in range(10):
    pass
print(i)
