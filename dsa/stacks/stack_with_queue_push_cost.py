import queue


class Stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, data):
        self.q2.put(data)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()
        return "stack is empty"

    def print_stack(self):
        print(self.q1.queue)


q = Stack()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.print_stack()
q.pop()
q.print_stack()
q.pop()
q.print_stack()
q.pop()
q.print_stack()
q.pop()
q.print_stack()
q.pop()
q.print_stack()
q.pop()
q.print_stack()
