# precision only applies to the mathematical operations but not the decimal const or storage of decimals
import decimal
from decimal import Decimal

print(decimal.getcontext())
decimal.getcontext().prec = 3
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
print(decimal.getcontext())
a = Decimal('2.52345')
b = Decimal('6.52345')
print(a, b, a + b)

x = Decimal('0.3')
print(format(x, '.30f'))
y = Decimal(0.3)
print(format(y, '.30f'))
print(Decimal(0.3))
