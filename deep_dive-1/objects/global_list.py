# [-5,256] is a singleton global list (interning)
a = 257
b = 257
print(a is b)  # should be false actually in cpython
