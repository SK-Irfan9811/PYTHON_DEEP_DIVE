# through global variable

global_list = []


def add_items():
    for i in range(1000):
        global_list.append(i)
def add_items1():
    for i in range(1000):
        global_list.append(i)
    global_list.clear()

def add_items2():
    for i in range(1000):
        global_list.append(i)
















# leads to memory bloat or memory leak as it keeps growing without freeing the memory that is no longer needed
# solution
global_list.clear()
# limit scope
# use weak references - that module allows you to create references to objects that don’t prevent them from being garbage-collected.
import weakref


class MyClass:
    def __init__(self, name):
        self.name = name


# Create an instance of MyClass
obj = MyClass('My Object')

# Create a weak reference to obj
# weak_ref = weakref.ref(obj)
obj1 = weakref.ref(obj)
# Access the object through the weak reference
# print(weak_ref())  # Output: <__main__.MyClass object at ...>

# Now delete the original reference
del obj


# Try accessing the weak reference again (it returns None, as the object has been garbage collected)
# print(weak_ref())  # Output: None
# print(obj1)

# Strong references: Prevent objects from being garbage-collected.
# Weak references: Allow you to reference objects without preventing their garbage collection


# through lingering references
# weak ref
# context manager




# closures and anonymous functions
def outer():
    a = "python"

    def inner():

        print("{0} rocks".format(a))

    return inner  # returning not just an function ,but closure


fn = outer()
fn()
print(fn.__code__.co_freevars)
print(fn.__closure__)
















# modifying free variables
# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inc
#
#
# # both f1 and f2 have different extended scopes
# f1 = counter()
# f2 = counter()
# f1()
# f2()


# shared extended scopes
# def counter():
#     count = 0
#
#     def inc1():
#         nonlocal count
#         count += 1
#         print(count)
#
#     def inc2():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inc1, inc2
#
#
# f1, f2 = counter()
# f1()
# f2()
# f1()
# f2()





# closure memory leak
def outer_function():
    large_list = [i for i in range(1000000)]

    def inner_function():
        return large_list[0]

    return inner_function


my_closure = outer_function()
