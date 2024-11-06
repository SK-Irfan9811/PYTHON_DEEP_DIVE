class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
        else:
            if self.head == self.tail:  # single element case
                self.tail = self.head = None
            else:
                self.head = self.head.next

    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return None
        return self.head.data

    def display_queue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        node = self.head
        while node.next is not None:
            print(node.data, "-->", end="")
            node = node.next
        print(node.data)


q = Queue()
q.enqueue(420)
q.enqueue(421)
q.enqueue(422)
q.enqueue(423)
q.enqueue(424)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.enqueue(500)
q.enqueue(600)
q.enqueue(700)
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
print(q.peek())
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.dequeue()
