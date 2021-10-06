# Implement a function to check if a tree is a binary search tree.

from traversals import inorder


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

# root.right.left = Node(11)
#                   (5)
#           (3)             (7)
#       (2)    (4)      (6)     (8)


stack = []


def validate_bst(root):
    if root is None:
        return None
    validate_bst(root.left)
    stack.append(root.data)
    validate_bst(root.right)


validate_bst(root)

print(stack)
i = 0

while i < len(stack) - 1:
    if stack[i + 1] - stack[i] < 0:
        print(False)
        break
    i += 1
else:
    print(True)


def validate_bst_without_stack(root, prev):
    if root is None:
        return True

    left = validate_bst_without_stack(root.left, prev)
    if root.data <= prev.data:
        return False

    prev.data = root.data

    right = validate_bst_without_stack(root.right, prev)

    return left and right


prev = Node(float("-inf"))
print(validate_bst_without_stack(root, prev))



def validate_bst_optimised(root, min_value, max_value):
    if root is None:
        return True

    if min_value > root.data or root.data >  max_value:
        return False
    
    left = validate_bst_optimised(root.left, min_value, root.data)
    right = validate_bst_optimised(root.right, root.data, max_value)

    return left and right


print(validate_bst_optimised(root,float("-inf"), float("inf")))
