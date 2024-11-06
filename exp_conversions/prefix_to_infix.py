class PrefixToInfix:
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

    def convert_to_infix(self, prefix_exp):
        modified_exp = "".join(list(reversed(prefix_exp)))
        for item in modified_exp:
            if item in self.operand_set:
                self.push(item)
            else:
                if item == '-' and len(self.__stack) == 1:
                    self.push('(' + item + self.pop() + ')')
                else:
                    first_item = self.pop()
                    second_item = self.pop()
                    self.push('(' + first_item + item + second_item + ')')
        return self.__stack.pop()
