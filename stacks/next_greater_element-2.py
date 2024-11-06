class NextGreaterElement:
    def __init__(self):
        self.__stack = []
        self.__ans = []

    def get_list_of_nges(self, lst):
        for ele_idx in range(len(lst)):
            for itr in range(ele_idx + 1, ele_idx + len(lst)):
                if lst[ele_idx] < lst[(itr % len(lst))]:
                    self.__ans.append(lst[(itr % len(lst))])
                    break
            else:
                self.__ans.append(-1)
        return self.__ans


nge = NextGreaterElement()
print(nge.get_list_of_nges([1, 2, 1]))
