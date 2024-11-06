import sys


class MinStackSpaceOptimized:
    def __init__(self):
        self.__min_stack = []
        self.min_value = sys.maxsize

    def push(self, item):
        if not self.is_empty():
            if self.min_value > item:
                self.__min_stack.append((2 * item) - self.min_value)
                self.min_value = item
            else:
                self.__min_stack.append(item)
        else:
            self.min_value = item
            self.__min_stack.append(item)

    def pop(self):
        if self.__min_stack[-1] < self.min_value:
            self.min_value = (2 * self.min_value) - self.__min_stack[-1]
        self.__min_stack.pop()

    def is_empty(self):
        return not self.__min_stack

    def get_min(self):
        return self.min_value

    def display_stck(self):
        for i in self.__min_stack:
            print(i, end=",")


ms = MinStackSpaceOptimized()
ms.push(10)
print(ms.min_value)
ms.push(20)
print(ms.min_value)
ms.push(15)
print(ms.min_value)
ms.push(9)
print(ms.min_value)
ms.push(8)
print(ms.min_value)
ms.pop()
print(ms.min_value)
ms.pop()
print(ms.min_value)
ms.pop()
print(ms.min_value)
ms.pop()
print(ms.min_value)
