class NextGreaterElement:
    def __init__(self):
        self.__stack = []
        self.ans = []

    def get_next_greater_element_list(self, lst):
        for i in lst[::-1]:
            if not self.__stack:
                self.ans.append({i: -1})
                self.__stack.append(i)
            else:
                while self.__stack and i >= self.__stack[-1]:
                    self.__stack.pop()
                if self.__stack:
                    self.ans.append({i: self.__stack[-1]})
                else:
                    self.ans.append({i: -1})
                self.__stack.append(i)

        return self.ans[::-1]


nge = NextGreaterElement()
print(nge.get_next_greater_element_list([1, 3, 4, 2]))
