import ctypes
import gc

gc.disable()


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(obj_id):
    for obj in gc.get_objects():
        if id(obj) == obj_id:
            return "object exists"
    return "object not found"


class A:
    def __init__(self):
        self.b = B(self)


class B:
    def __init__(self, a):
        self.a = a


my_var = A()
a_id = (id(my_var))
b_id = (id(my_var.b))

print("refcount of A -", ref_count(a_id))
print("refcount of B -", ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
gc.collect()

print("refcount of A -", ref_count(a_id))
print("refcount of B -", ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

# random code
p = [101010, 1010]
p_id = id(p)
p = None
print(ref_count(p_id))
