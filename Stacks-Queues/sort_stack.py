# Writa a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure(such asa an array). the stack supports the
# following operations: push, pop, peeka dn isEmpty.


class SortStack:
    def __init__(self) -> None:
        self.stack = []
    
    def peek(self):
        pass

    def isEmpty(self):
        return len(self.satck) == 0
    
    def sort_stack(self):
        temp_stack = []

        while self.stack:
            temp = self.stack.pop()

            while temp_stack and temp_stack[-1] > temp:
                self.stack.append(temp_stack.pop())
            temp_stack.append(temp)
        while temp_stack:
            self.stack.append(temp_stack.pop())


stack = SortStack()

stack.stack.append(10)
stack.stack.append(3)
stack.stack.append(0)
stack.stack.append(19)


print(stack.stack)

stack.sort_stack()

print(stack.stack)