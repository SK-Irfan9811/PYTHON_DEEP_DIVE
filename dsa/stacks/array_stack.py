class Stack:
    def __init__(self):
        self.__top = -1
        self.__stk = []

    def push(self, item):
        self.__stk.append(item)
        self.__top += 1

    def pop(self):
        try:
            item = self.__stk[self.__top]
            self.__stk.remove(item)
            self.__top -= 1
            return item
        except IndexError as e:
            print("No more items to pop out - ", e.__class__.__name__)

    def peek(self):
        try:
            print(self.__stk[self.__top])
        except IndexError as e:
            print("No more items to peek - ", e.__class__.__name__)

    def is_empty(self):
        return self.__top == -1

    def display_stack(self):
        print(self.__stk)


stack1 = Stack()
stack2 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.peek()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.peek()
stack1.display_stack()
stack2.push("ERROR")
stack2.push("SUCCESS")
stack2.push("FAILURE")
stack2.display_stack()
