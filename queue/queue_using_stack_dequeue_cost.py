class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")

        if not self.stack2:
            # Transfer all elements from stack1 to stack2 only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")

        if not self.stack2:
            # Transfer all elements from stack1 to stack2 only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        # A helper function to check if the queue is empty
        return not self.stack1 and not self.stack2


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
