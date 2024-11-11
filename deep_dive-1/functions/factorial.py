def factorial(n, cache={}):
    if n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f"calculating {n} !")
        result = n * factorial(n - 1)
        cache[n] = result
        return result


print(factorial(5))
print(factorial(6))

# here cache dict is shared to all func calls amd is local to function and is mutable

# def f(f):
#     print(f)
# f=1
# # f(f) f lable is now pointing to th integer value which is not callable as function
# print(f)
d = {1: 2, 2: 4, 3: 8}
print(d.values())
print(d.keys())
print(d.items())

