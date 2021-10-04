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

