# class Logger:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#         return cls._instance
#
#
# l1 = Logger()
# l2 = Logger()
# print(l1 is l2)
#
#
# def singleton_decor(cls):
#     instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
#
# @singleton_decor
# class Singleton:
#     pass
#
#
# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)
# a = [1, 2, 3]
# b = a[:]
# print(a is b)
# class goutham:
#     pass
# print(type(type))
# import json
#
# d = {"a": 1, "b": 2}
# print(type(json.loads(json.dumps(d))))
a=[1,2,3,[1,2,3,4,5,6]]
b=a.copy()
del a[3]
print(a,b)
