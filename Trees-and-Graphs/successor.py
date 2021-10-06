# Write an algorithm to find the "next" node (i.e., in-order successor) of a
# given node in a binary tree. You may assume each nod ehas link to parent
# node


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = Node(5)

root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.left = Node(6)
root.right.right = Node(8)

#                   (5)
#           (3)             (7)
#       (2)    (4)      (6)     (8)


def find_successor(root, element):
    successor = None
    while root.data != element:
        if root.data > element:
            successor = root
            root = root.left
        else:
            root = root.right

    if root.right:
        root = root.right
        while root.left:
            root = root.left

        return root.data
    else:
        if successor:
            return successor.data
        else:
            return None


print(find_successor(root, 2))
print(find_successor(root, 3))
print(find_successor(root, 4))
print(find_successor(root, 5))
print(find_successor(root, 8))


