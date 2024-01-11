from _decimal import Decimal

a = int(10)
b = int(-10.23)
print(a, b)
print(int(Decimal("10.9")))
print(int("23"))
print(int("10F", base=16))
print(int("A", base=11))  # 11 is explicit here
print(int(0xF))
print(int('88', 36))
