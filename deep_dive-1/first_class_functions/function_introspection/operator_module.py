import operator
from functools import reduce

print(dir(operator))
_add = lambda a, b: operator.add(a, b)
_mul = lambda a, b: operator.mul(a, b)
_pow = lambda a, b: operator.pow(a, b)
_mod = lambda a, b: operator.mod(a, b)
_floordiv = lambda a, b: operator.floordiv(a, b)
_neg = lambda a: operator.neg(a)

print(reduce(_add, [1, 2, 3, 4, 5]))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(operator.getitem(lst, 4))
operator.setitem(lst, 4, 100)
print(lst)
operator.delitem(lst, 6)
print(lst)

# itemgetter(kind of partial function)
first_item_getter = operator.itemgetter(1)
print(first_item_getter((1, 2, 3, 4)))


class MyClass:
    b = 900

    def __init__(self):
        self.a = 10
        self.b = 20

    @classmethod
    def test_cls(cls):
        print("class meth is running")

    def test(self,c):
        print("test meth is running",c)


attrcaller = operator.attrgetter('b')
print(attrcaller(MyClass))
print(attrcaller(MyClass()))
test_caller = operator.methodcaller("test",10)
cls_test_caller = operator.methodcaller("test_cls")
test_caller(MyClass())
cls_test_caller(MyClass())
