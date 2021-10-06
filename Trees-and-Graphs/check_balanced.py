# Implement a function to check if a binary tree is balanced. For the purpose
# of this question, a balanced tree is defined to be a tree such that the
# heights of the two subtrees of any node never differ by more than one.


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.left.left = Node(11)

root.right.right.right = Node(9)
root.right.right.right.right = Node(10)
#                   (1)
#           (2)             (3)
#       (4)    (5)      (6)     (7)
# (8)                                   (9)
#                                               (10)
print(get_height(root))


def is_balanced(root: Node):
    if root is None:
        return True

    height = get_height(root.left) - get_height(root.right)

    if abs(height) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


print(is_balanced(root))


def is_balanced_optimised(root, is_balanced=True):
    if root is None or not is_balanced:
        return -1, is_balanced

    left_height, is_balanced = is_balanced_optimised(root.left, is_balanced)
    right_height, is_balanced = is_balanced_optimised(root.right, is_balanced)

    if abs(left_height - right_height) > 1:
        is_balanced = False
    return max(left_height, right_height) + 1, is_balanced


print(is_balanced_optimised(root))
