class InfixToPostfix:
    operand_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    priority_map = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '%': 2,
        'u-': 4
    }

    def __init__(self):
        self.__stack = []
        self.__ans = ""
        self.last_char = None

    def is_empty(self):
        return len(self.__stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()

    def get_priority(self, operator):
        return self.priority_map.get(operator, None)

    def pop_until_open_brace(self):
        while self.peek() != "(":
            self.__ans += self.pop()
        self.pop()

    def pop_until_low_priority_item_appears(self, item):
        if not self.is_empty() and self.get_priority(self.peek()) >= self.get_priority(item):
            while not self.is_empty() and self.get_priority(self.peek()) >= self.get_priority(item):
                self.__ans += self.pop()
        self.push(item)

    def convert_to_postfix(self, infix_exp):
        for item in infix_exp:
            if item in self.operand_set:
                self.__ans += item
                self.last_char = item
            else:
                if item == '-' and (self.last_char is None or self.last_char in '(-+*/'):
                    item = 'u-'
                if self.is_empty() or item == "(":
                    self.push(item)
                elif item == ")":
                    self.pop_until_open_brace()
                else:
                    self.pop_until_low_priority_item_appears(item)
            self.last_char = item

        while not self.is_empty():
            self.__ans += self.pop()
        self.__ans = self.__ans.replace('u-', '-')
        return self.__ans
