# Implement linked list


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print()
    def _length_recursive(self, node: Node):
        if not node:
            return 0
        else:
            return 1 + self._length_recursive(node.next)

    def length(self):
        return self._length_recursive(self.head)
