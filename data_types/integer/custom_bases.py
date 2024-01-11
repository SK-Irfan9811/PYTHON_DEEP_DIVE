def from_base10(num, base):
    digits = []

    while num > 0:
        num, digit = divmod(num, base)
        digits.insert(0, digit)
    return digits


def encode(digits, digit_map):
    if max(digits) > len(digit_map):
        raise ValueError("digit map is not long enough to encode the digits")
    encoding = ''.join(digit_map[d] for d in digits)
    return encoding


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 0 or base > 36:
        raise ValueError("base must be in 2-36 or 0")
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        return "-" + encoding
    return encoding


print(rebase_from10(232, 5))
print(rebase_from10(119, 12))
print(rebase_from10(255, 16))
print(rebase_from10(71, 36))
print(rebase_from10(314, 2))
print(rebase_from10(-254, 2))
n = eval(input())
print(n)
