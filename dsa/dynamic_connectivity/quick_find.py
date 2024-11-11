class QuickFind:
    """
    This approach assumes that two elements are connected if they have the same value., both element and it's index.
    Takes constant time for finding the connectivity.
    Union in the worst case takes quadratic time as elements have to be replaced for every union operation.
    """

    def __init__(self, n):
        self.__arr = [x for x in range(n)]

    def union(self, first, second):
        first = self.__arr[first]
        second = self.__arr[second]

        for ele in range(len(self.__arr)):
            if self.__arr[ele] == first:
                self.__arr[ele] = second

    def is_connected(self, first, second):
        return self.__arr[first] == self.__arr[second]

    def print_array(self):
        print(self.__arr)


q = QuickFind(5)
q.union(2, 4)
q.union(0, 4)
q.union(4, 1)
q.print_array()
