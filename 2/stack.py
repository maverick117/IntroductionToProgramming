class Stack:
    def __init__(self,size):
        self.elements = [0 for _ in range(size)]
        self.size = size
        self.count = 0

    def push(self,sth):
        if(self.count == self.size):
            return
        else:
            self.elements[self.count] = sth
            self.count += 1

    def pop(self):
        if(self.count <= 0):
            return None
        else:
            self.count -= 1
            return self.elements[self.count]

    def isEmpty(self):
        return (self.count == 0)

    def isFull(self):
        return (self.count == self.size)


stack = Stack(5)
stack.push(1)
stack.push(5)
stack.push(7)
stack.push(3)
stack.push(6)

while not stack.isEmpty():
    print(stack.pop())
