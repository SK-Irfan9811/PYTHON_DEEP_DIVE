import ctypes
import sys

# using getrefcount(), accepts variable name as parameter
p1 = [1, 2, 3]
p2 = p1
print(sys.getrefcount(p1))
# p1 = None
# print(sys.getrefcount(p2))




















# p2 = None
# print(sys.getrefcount(p1))
# passing the variable to getrefcount() creates another reference to the location where [1,2,3] is stored


# this technique accepts the address of a value, so no more references are created, thus giving accurate ref count
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


p_id = id(p1)

print(p_id)
print(ref_count(p_id))
p1 = None
p2=None
print(ref_count(p_id))

