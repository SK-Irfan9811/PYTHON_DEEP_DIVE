def func(a: str = 'sk',
         *args: 'any addn params',
         b: int = 1,
         **kwargs: 'adn keyword args') -> int:
    pass


print(func.__annotations__)
