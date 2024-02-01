# print(True == 1, True is 1)
# print(False == 0, False is 0)
print(issubclass(bool, int))
# print(isinstance(bool, 1))
print(isinstance(False, bool))
print(False is bool(0), id(False))
# bool objs are singleton objects
print(True > False)
print((1 == 2) == 0)
print(1 == 2 == False)  # equivalent to 1==2 and 2==False
# empty sequence is false
print(bool([]))
print(bool([1]))
print(bool([None]))
print(bool([0]))
print(bool(None))
print(bool(''))
print(bool(' '))
print(bool(-1))
print((0).__bool__())
print((0.1).__bool__())
a = []
print(a.__len__())
print(bool(a))  # invokes __len__() method
a = " "
if a:  # a is equivalent to bool(a)
    print("a is something")
else:
    print("nothing here")
a = None
if a is not None and len(a):  # none has no len()
    print("hello")
print(bool(a))
