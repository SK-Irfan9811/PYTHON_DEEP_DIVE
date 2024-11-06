class PrefixToPostfix:
    operand_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def is_empty(self):
        return not len(self.__stack)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]

    def convert_to_postfix(self, prefix_exp):
        for item in prefix_exp[::-1]:
            if item in self.operand_set:
                self.push(item)
            else:
                second_op = self.pop()
                first_op = self.pop()
                self.push(second_op + first_op + item)
        return self.pop()
