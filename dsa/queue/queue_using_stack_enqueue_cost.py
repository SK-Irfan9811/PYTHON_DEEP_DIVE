class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enqueue(self, data):
        while self.stk1:
            self.stk2.append(self.stk1.pop())

        self.stk1.append(data)

        while self.stk2:
            self.stk1.append(self.stk2.pop())

    @staticmethod
    def is_empty(lst):
        return len(lst) == 0

    def dequeue(self):
        if not self.is_empty(self.stk1):
            return self.stk1.pop()

    def peek(self):
        if not self.is_empty(self.stk1):
            return self.stk1[-1]

    def display_queue(self):
        print(self.stk1)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
print(q.peek())
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
q.dequeue()
q.display_queue()
