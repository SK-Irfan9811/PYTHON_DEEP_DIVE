# def func(a: 'a number', b: 'a string') -> 'a string':
#     return a * b
#
#
# print(func(3, 'irfan '))
# print(func.__doc__)
# print(help(func))


# def func_1(a: str, b: [1, 2, 3, 4]) -> int:
#     return a * b
#
#
# print(func_1(2, 6))

a = 3
b = 5


def func_2(a: str, b: int) -> 'a repeated ' + str(a) + ' times':
    """hello this is function-2"""
    return a * b


print(help(func_2))
print(func_2(2, 6))
print(func_2(5, 6))


# def func_3(a: str = 'sk',
#            *args: 'any addn params',
#            b: int = 1,
#            **kwargs: 'adn keyword args') -> str:
#     pass
# print(func_3())

