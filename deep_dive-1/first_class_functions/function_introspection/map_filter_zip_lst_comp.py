#  map(func,*iterables)  is a higher order function
# def fact(n):
#     return 1 if n < 2 else n * fact(n - 1)
#
#
# results = map(fact, range(15))
# print(list(results))  # it gets consumed here itself and an empty list is remained
# print(list(results))
#
# # another example
# res = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6], [7, 8, 9])
# print(res)  # no error
# print(list(res))  # raises TypeError as the python now tries to access the elements of the map object of type iterator

# print = lambda x:x+10
# x=print(9)
# print(x)




def my_fun():
    print(a)
    global a
    a = "SK"
    print(a)


my_fun()
