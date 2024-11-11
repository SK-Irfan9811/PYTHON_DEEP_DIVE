class PostfixToInfix:
    operand_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    def __init__(self):
        self.__stack = []

    def convert_to_infix(self, postfix_exp):
        for item in postfix_exp:
            if item in self.operand_set:
                self.__stack.append(item)
            else:
                if item == '-' and len(self.__stack) == 1:
                    self.__stack.append("(" + item + self.__stack.pop() + ")")
                else:
                    second_opnd = self.__stack.pop()
                    first_opnd = self.__stack.pop()
                    self.__stack.append('(' + first_opnd + item + second_opnd + ')')

        return self.__stack.pop()

