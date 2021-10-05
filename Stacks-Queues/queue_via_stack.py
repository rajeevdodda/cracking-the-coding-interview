# Implement a MyQueue class which implements using two stacks

class MyQueue:
    def __init__(self) -> None:
        self._stack_1 = []
        self._stack_2 = []


    def enqueue(self, data):
        self._stack_1.append(data)
    
    def dequeu(self):
        while self._stack_1:
            self._stack_2.append(self._stack_1.pop())
        
        temp = self._stack_2.pop()
        
        while self._stack_2:
            self._stack_1.append(self._stack_2.pop())
        
        return temp
    

q = MyQueue()

for i in range(10):
    q.enqueue(i)

print(q.dequeu())

class MyQueueOptimized:
    def __init__(self) -> None:
        self.stack_new = []
        self.stack_old = []

    def size(self):
        return len(self.stack_new) + len(self.stack_old)
    
    def shuffle(self):
        if not self.stack_old:
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())
    
    def peek(self):
        self.shuffle()
        return self.stack_old[-1]

    def enqueue(self, data):
        self.stack_new.append(data)

    def dequeue(self):
        self.shuffle()
        return self.stack_old.pop()



qq = MyQueueOptimized()

qq.enqueue(10)
qq.enqueue(9)
print(qq.stack_new, qq.stack_old)
print(qq.peek())
qq.enqueue(11)
print(qq.stack_new, qq.stack_old)
qq.enqueue(12)


