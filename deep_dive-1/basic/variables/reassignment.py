import ctypes
import sys


def ref_count(address):
    return ctypes.c_long.from_address(address).value


var = 10
print(hex(id(var)))
var1_add = id(var)
print(sys.getrefcount(var1_add) - 1)

var = 15
print(hex(id(var)))
var2_add = id(var)
print(sys.getrefcount(var2_add) - 1)

var += 5
print(hex(id(var)))
var3_add = id(var)
print(sys.getrefcount(var1_add) - 1)

print("ref counts of all address-{0},{1},{2}".format(ref_count(var1_add)
                                                     , ref_count(var2_add)
                                                     , ref_count(var3_add)))
a = 10
b = 10
print(hex(id(a)), hex(id(b)))
