
class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            return self.queue[0]

    def display(self):
        print(self.queue)


q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

print("Front element:", q.peek())
