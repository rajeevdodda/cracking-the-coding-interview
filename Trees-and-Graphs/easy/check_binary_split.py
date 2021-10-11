# https://www.techiedelight.com/split-binary-tree-into-two-trees/

# Check if removing an edge can split a binary tree into two equal size trees


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)


def count_nodes(root):
    if root is None:
        return 0
    count = 1 + count_nodes(root.left) + count_nodes(root.right)
    return count


def check_binary_split(root):
    print(count_nodes(root) % 2 == 0)


check_binary_split(root)