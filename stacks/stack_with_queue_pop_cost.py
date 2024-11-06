import queue


class Stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, data):
        self.q1.put(data)

    def pop(self):
        if len(self.q1.queue) != 0:
            while len(self.q1.queue) != 1:
                self.q2.put(self.q1.get())
            popped_item = self.q1.get()
            while not self.q2.empty():
                self.q1.put(self.q2.get())
        else:
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
