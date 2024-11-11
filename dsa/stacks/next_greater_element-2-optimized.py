class NextGreaterElement:
    def __init__(self):
        self.__stack = []
        self.ans = []

    def get_nges(self, lst):
        n = len(lst)
        for i in range(((2 * n) - 1), -1, -1):
            while self.__stack and lst[(i % n)] >= self.__stack[-1]:
                self.__stack.pop()
            if i < n:
                self.ans.append(self.__stack[-1]) if self.__stack else self.ans.append(-1)
            self.__stack.append(lst[(i % n)])
        return self.ans[::-1]


nge = NextGreaterElement()
print(nge.get_nges([2, 10, 12, 1, 11]))
