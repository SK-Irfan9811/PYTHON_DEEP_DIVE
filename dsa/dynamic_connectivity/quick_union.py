from typing import List


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


class QuickUnion:

    def __init__(self):
        self.ans: List[LinkedList] = []

    def union(self, ele1, ele2):
        if ele1 == ele2:
            if ele1 not in [ele.data for ele in self.ans]:
                self.ans.append(LinkedList(ele2))
        elif ele1 != ele2:
            if ele1 not in [ele.data for ele in self.ans]:
                child = LinkedList(ele1)
                self.ans.append(child)
            else:
                child_idx = [ele.data for ele in self.ans].index(ele1)
                child = self.ans[child_idx]
            if ele2 not in [ele.data for ele in self.ans]:
                parent = LinkedList(ele2)
                self.ans.append(parent)
            else:
                parent_idx = [ele.data for ele in self.ans].index(ele2)
                parent = self.ans[parent_idx]
            parent_root = self.__root(parent)
            child_root = self.__root(child)
            print(child_root.data, parent_root.data)
            if parent_root.data != child_root.data:
                child_root.next = parent_root

    @staticmethod
    def print_linked_list(node):
        while node.next is not None:
            print(node.data, "-->", end=" ")
            node = node.next
        print(node.data)

    def is_connected(self, ele_1, ele_2):
        node_1 = None
        node_2 = None
        for i in self.ans:
            if i.data == ele_1:
                node_1 = i
            if i.data == ele_2:
                node_2 = i
        if node_1 is None or node_2 is None:
            raise RuntimeError("element is not present")
        return self.__root(node_1) == self.__root(node_2)

    @staticmethod
    def __root(node):
        while node.next is not None:
            node = node.next
        return node


q = QuickUnion()
q.union(4, 3)
q.union(3, 8)
q.union(6, 5)
q.union(9, 4)
q.union(2, 1)
q.union(8, 9)
q.union(5, 0)
q.union(7, 2)
q.union(6, 1)
q.union(7, 3)
for i in q.ans:
    q.print_linked_list(i)
