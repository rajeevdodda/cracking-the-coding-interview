# Construct a complete binary tree from its linked list representation
from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)


# 1 > 2 > 3 > 4 > 5 > 6


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def convert_to_binary_tree(head: Node):
    if head is None:
        return None
    
    root = Tree(head.data)

    head = head.next

    q = deque()
    q.append(root)

    while head:
        node = q.popleft()
        node.left = Tree(head.data)
        q.append(node.left)
        head = head.next

        if head:
            node.right = Tree(head.data)
            q.append(node.right)
            head = head.next

    return root

#                 1
#           2           3
#       4      5     6

root = convert_to_binary_tree(head)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="->")
        inorder(root.right)


inorder(root)


