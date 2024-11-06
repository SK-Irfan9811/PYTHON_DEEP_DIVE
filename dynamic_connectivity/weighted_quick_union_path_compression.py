from typing import List


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


class QuickUnionOptimized:

    def __init__(self, n):
        self.ans: List[LinkedList] = []
        self.weight: List[int] = [0 for i in range(n)]

    def union(self, p, q):
        if p == q:
            if p not in [ele.data for ele in self.ans]:
                self.ans.append(LinkedList(p))
        elif p != q:
            if p not in [ele.data for ele in self.ans]:
                node_1 = LinkedList(p)
                self.ans.append(node_1)
            else:
                node1_idx = [ele.data for ele in self.ans].index(p)
                node_1 = self.ans[node1_idx]
            if q not in [ele.data for ele in self.ans]:
                node_2 = LinkedList(q)
                self.ans.append(node_2)
            else:
                node2_idx = [ele.data for ele in self.ans].index(q)
                node_2 = self.ans[node2_idx]
            root_1 = self.__root(node_1)
            root_2 = self.__root(node_2)
            parent, child = self.get_parent_child(root_1, root_2)
            child.next = parent
            if self.weight[child.data]:
                self.weight[parent.data] += self.weight[child.data]
            else:
                self.weight[parent.data] += 1

    def get_parent_child(self, root_1, root_2):
        if self.weight[root_1.data] >= self.weight[root_2.data]:
            child = root_2
            parent = root_1
        else:
            parent = root_2
            child = root_1
        return parent, child

    @staticmethod
    def print_linked_list(node):
        while node.next is not None:
            print(node.data, "-->", end=" ")
            node = node.next
        print(node.data)

    def is_connected(self, ele_1, ele_2):
        node_1 = None
        node_2 = None
        for node in self.ans:
            if node.data == ele_1:
                node_1 = node
            if node.data == ele_2:
                node_2 = node
        if node_1 is None or node_2 is None:
            raise RuntimeError("Element is not present")
        return self.__root(node_1) == self.__root(node_2)

    def __root(self, node):  # path compression
        if node.next is None:
            return node
        root = self.__root(node.next)
        node.next = root
        return root


q = QuickUnionOptimized(10)
q.union(4, 3)
q.union(3, 8)
q.union(6, 5)
q.union(9, 4)
q.union(2, 1)
q.union(5, 0)
q.union(7, 2)
q.union(6, 1)
q.union(7, 3)

for i in q.ans:
    q.print_linked_list(i)

print(q.weight)
print(q.is_connected(2, 7))
print(q.is_connected(1, 7))
print(q.is_connected(8, 6))

for i in q.ans:
    q.print_linked_list(i)
