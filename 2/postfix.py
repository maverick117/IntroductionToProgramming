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

def main():
    exp = input().split()
    stack = Stack(100)
    for token in exp:
        try:
            a = int(token)
            stack.push(a)
        except:
            a = stack.pop()
            b = stack.pop()
            c = 0
            if token == '+':
                c = b + a
            elif token == '-':
                c = b - a
            elif token == '*':
                c = b * a
            elif token == '/':
                c = b // a
            stack.push(c)
    print(stack.pop())

main()
