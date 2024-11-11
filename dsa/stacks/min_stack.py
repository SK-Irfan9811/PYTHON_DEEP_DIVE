class MinStack:
    def __init__(self):
        self.__min_stack = []

    def push(self, item):
        if self.is_empty():
            self.__min_stack.append({item: item})
        else:
            min_so_far = self.peek().get(next(iter(self.peek())))
            self.__min_stack.append({item: min(item, min_so_far)})

    def pop(self):
        if not self.is_empty():
            next(iter(self.__min_stack.pop()))

    def is_empty(self):
        return not self.__min_stack

    def peek(self):
        if not self.is_empty():
            return self.__min_stack[-1]

    def get_min(self):
        return self.peek().get(next(iter(self.peek())))

    def display_stack(self):
        print(self.__min_stack)


s = MinStack()
s.push(10)
s.push(12)
print(s.get_min())
s.push(1)
print(s.get_min())
s.push(16)
s.push(1)
s.push(-11)
print(s.get_min())
s.push(-10)
print(s.get_min())
s.push(100)
s.push(-100)
s.push(1)
s.push(-10)
s.pop()
print(s.get_min())
s.display_stack()
