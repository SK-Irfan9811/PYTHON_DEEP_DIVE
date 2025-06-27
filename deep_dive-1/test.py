# from abc import ABC, abstractmethod
# try:
#     print(1/0)
# except Exception:
#     print("Parent")
# except ZeroDivisionError:
#     print("Zero...")
# else:
#     print("no erroes")
# finally:
#     print("rer")
#
#
# str_="PYTHON"
# print(str_[2:])
# class Test:
#     continue
# for i in [1,2,3,4,5,6]:
#     if i%2==0:
#         continue
#     print("Hii",i)
from abc import abstractmethod, ABC


# c
class A(ABC):
    @abstractmethod
    def m(self):
        print("A")


class B(A):
    pass


# a=A()
b = B()
b.m()
