import decimal

from _decimal import Decimal

dec_ctx = decimal.getcontext()
# local and global contexts
# print(type(decimal.localcontext()))
# print(type(decimal.getcontext()))
print(dec_ctx)
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
    print(id(ctx) == id(decimal.getcontext()))
