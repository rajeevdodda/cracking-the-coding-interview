# How would you design a stack which, in addition to push and pop, has a 
# fucntion "min" which returns the minimum element? Push, Pop, min should 
# all operate in O(1)

class Stack:
    def __init__(self) -> None:
        self._data = []
        self.min_value = float("inf")
    
    def push(self, element):
        self.min_value = min(self.min_value, element)
        self._data.append((element, self.min_value))
    
    def pop(self):
        element, min_value = self._data.pop()
        if element == self.min_value:
            self.min_value = self._data[-1][1]
        return element
    
    def min_element(self):
        return self.min_value



s = Stack()


for i in range(10):
    s.push(i)

s.push(-10)
print(s._data)
print(s.min_element())
s.pop()
print(s.min_element())
print(s._data)
