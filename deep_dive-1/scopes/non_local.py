# 1
# def outer1():
#     print("outer")
#
#     def inner1():
#         print("inner")
#
#     inner1()
#
#
# outer1()


# referencing global variable inside function
# a = 10
# def outer():
#     print(a)
#
#
# outer()

# non local
# def outer():
#     a = 10
#
#     def inner():
#         print(a)
#
#     inner()
#
#
# outer()

#  non local var
# def outer():
#     x = "Monty"
#     print(x)
#
#     def inner():
#         x = "Python"  # local variable as assignment is encountered
#         print(x)
#
#     inner()
#
#
# outer()

# modifying non local var
# def outer():
#     x = "Python"
#
#     def inner():
#         nonlocal x
#         x = "Java"
#
#     print(x)
#     inner()
#     print(x)
#
#
# outer()

# multiple non locals
# def outer():
#     x = 10
#
#     def inner1():
#         nonlocal x
#         x = 20
#
#         def inner2():
#             nonlocal x
#             x = 30
#         print(x)
#         inner2()
#         print(x)
#     print(x)
#     inner1()
#     print(x)


# outer()

# x=100
# def outer():
#     x="py"
#     def inner1():
#         nonlocal x
#         x="Monty"
#         def inner2():
#             global x
#             x=200
#         print(x)
#         inner2()
#         print(x)
#     print(x)
#     inner1()
#     print(x)
# print(x)
# outer()
# print(x)

#non local won't create any variable if not present in the enclosing scopes
# def outer():
#     global x
#     x="Monty"
#     def inner():
#         nonlocal x
#         x="Python"
#     inner()
# outer()


