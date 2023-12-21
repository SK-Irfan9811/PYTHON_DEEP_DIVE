var = 10
print(type(var))

var = 'hello'
print(type(var))

# the above var does not have any data type, it is just a ref to the memory address of specific
# type and that type is being printed when we call type()

lm = lambda a: a ** 2
print(lm(2))
print(type(lm(2)))
print(type(lm))
