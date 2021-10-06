# Given a sorted (increasing order) array with unique integer elements, write
# an algorithm to create a binary search tree with minimal height

from traversals import inorder

elements = list(range(1, 10))

print(elements)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def minimal_tree(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = minimal_tree(array, start, mid - 1)
    root.right = minimal_tree(array, mid + 1, end)
    return root


root = minimal_tree(elements, 0, len(elements) - 1)



inorder(root)