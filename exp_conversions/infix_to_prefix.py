class InfixToPrefix:
    operand_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    priority_map = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '%': 2,
        '_': 4
    }

    def __init__(self):
        self.__ans = ""
        self.__stack = []
        self.last_char = None

    def get_priority(self, operator):
        return self.priority_map.get(operator, None)

    def modify_exp(self, exp):
        exp = list(exp)
        for idx in range(len(exp)):
            if exp[idx] == '-' and (self.last_char is None or self.last_char in '(-+*/'):
                exp[idx] = '_'
            if exp[idx] == '(':
                exp[idx] = ')'
            elif exp[idx] == ')':
                exp[idx] = '('
            self.last_char = exp[idx]
        exp = list(reversed(exp))
        return "".join(exp)

    def is_empty(self):
        return len(self.__stack) == 0

    def peek(self):
        return self.__stack[-1]

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()

    def pop_until_open_brace(self):
        while not self.is_empty() and self.peek() != "(":
            self.__ans += self.pop()
        self.pop()

    def pop_until_low_priority_item_appears(self, item):
        if not self.is_empty() and (self.get_priority(self.peek()) > self.get_priority(item)):
            while not self.is_empty() and (self.get_priority(self.peek()) > self.get_priority(item)):
                self.__ans += self.pop()
        self.push(item)

    def convert_to_prefix(self, infix_exp):
        modified_infix = self.modify_exp(infix_exp)
        print(modified_infix)
        for item in modified_infix:
            if item in self.operand_set:
                self.__ans += item
            else:
                if self.is_empty() or item == '(':
                    self.push(item)
                elif item == ')':
                    self.pop_until_open_brace()
                elif item == '^':
                    if not self.is_empty() and (self.get_priority(self.peek()) >= self.get_priority(item)):
                        while not self.is_empty() and (self.get_priority(self.peek()) >= self.get_priority(item)):
                            self.__ans += self.pop()
                    self.push(item)

                else:
                    self.pop_until_low_priority_item_appears(item)
        while not self.is_empty():
            self.__ans += self.pop()
        self.__ans = self.__ans.replace('_', '-')
        return "".join(reversed(self.__ans))
