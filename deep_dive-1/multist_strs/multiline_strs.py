st = """This 
is a multiline st"""
print(st)


def my_func():
    # here it seems we are breaking indentation, but not.it is a single entity.
    a = """this is 
multiline"""
    return a


print(my_func())
