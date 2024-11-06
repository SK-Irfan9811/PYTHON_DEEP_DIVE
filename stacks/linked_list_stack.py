class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, item):
        node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        popped_node = self.top
        popped_item = popped_node.data
        self.top = self.top.next
        self.size -= 1
        popped_node.next = None
        return popped_item

    def display_stack(self):
        if not self.is_empty():
            node = self.top
            while node.next is not None:
                print(node.data, "-->", end="")
                node = node.next
            print(node.data)

        else:
            print("stack is empty")
            return None

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return -1
        return self.top.data


if __name__ == "main":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    stack.pop()
    stack.display_stack()
    stack.push("A")
    stack.push("B")
    stack.display_stack()
