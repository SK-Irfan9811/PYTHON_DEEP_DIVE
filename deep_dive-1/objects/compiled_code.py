import dis


def fun(a, b):
    return a + b


print(dis.dis(fun))
