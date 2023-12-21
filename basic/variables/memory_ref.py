import ctypes
import sys

my_var = 10
# here my_var is referencing to the address where 10 is stored
print(my_var)
print(id(my_var))
print(hex(id(my_var)))
my_lst = [1, 2, 3]
lst = my_lst
print(sys.getrefcount(my_lst))


# gives exact ref count
def ref_count(address):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(my_lst)))
x = [2, 3, 4]
x_id = id(x)
print(ref_count(x_id))
x = None
print(ref_count(x_id))
