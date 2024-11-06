class Queue:
    def __init__(self):
        self.__q = []

    def enqueue(self, data):
        self.__q.append(data)

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        ele = self.__q[0]
        self.__q.remove(ele)
        return ele

    def is_empty(self):
        return self.get_size() == 0

    def get_size(self):
        return len(self.__q)

    def display_queue(self):
        print(self.__q)


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.display_queue()
q1.dequeue()
q1.display_queue()
q1.dequeue()
q1.display_queue()
q1.dequeue()
q1.display_queue()
q1.dequeue()
q1.display_queue()
q1.dequeue()
