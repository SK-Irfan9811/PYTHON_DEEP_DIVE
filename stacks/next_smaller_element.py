class PreviousSmallerElement:
    def __init__(self):
        self.__ans = []
        self.__stack = []

    def get_previous_smaller_elements(self, lst):
        self.__stack.append(lst[0])
        self.__ans.append(-1)
        for ele in lst[1:]:
            while self.__stack and self.__stack[-1] >= ele:
                self.__stack.pop()
            self.__ans.append(self.__stack[-1]) if self.__stack else self.__ans.append(-1)
            self.__stack.append(ele)
        return self.__ans


p = PreviousSmallerElement()
print(p.get_previous_smaller_elements([3, 2, 1]))
