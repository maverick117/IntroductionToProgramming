class Queue:
    def __init__(self,size):
        self.data = [0 for _ in range(size+1)]
        self.size = size + 1
        self.head = 0
        self.tail = 0

    def dequeue(self):
        if self.head == self.tail:
            print("Queue is empty!")
        else:
            ret = self.data[self.tail]
            self.tail = (self.tail + 1) % self.size
            return ret
    
    def enqueue(self,sth):
        if self.tail  == (self.head + 1) % self.size:
            print("Queue is full!")
        else:
            self.data[self.head] = sth
            self.head = (self.head + 1) % self.size

    def isempty(self):
        return self.head == self.tail

    def isfull(self):
        return self.tail == (self.head + 1) % self.size

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
while not queue.isempty():
    print(queue.dequeue())
