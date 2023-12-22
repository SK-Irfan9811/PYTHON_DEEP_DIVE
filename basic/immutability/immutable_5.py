def process(var):
    print("initial id: ", id(var))
    var += 'hello'
    print("final id: ", id(var))
    return var


var = 'hi'
print("before modification id: ", id(var))
process(var)
print("after modification id: ", id(var))
