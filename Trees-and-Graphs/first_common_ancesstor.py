# Design an algorithm and write code to find the first common ancestor of two
# nodes in a binary tre. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.


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


def get_path(root: Node, node: Node):
    path = []

    while root.data != node:
        path.append(root.data)
        if root.data > node:
            root = root.left
        else:
            root = root.right

    path.append(root.data)

    return path


def lca_using_array(root: Node, node_a, node_b):
    path_a = get_path(root, node_a)
    path_b = get_path(root, node_b)

    lca = None

    i = 0

    while i < len(path_a) and i < len(path_b):
        if path_a[i] == path_b[i]:
            lca = path_a[i]
        i += 1
    print(lca)


lca_using_array(root, 2, 8)
lca_using_array(root, 2, 5)
lca_using_array(root, 4, 7)
lca_using_array(root, 3, 6)
lca_using_array(root, 2, 4)
lca_using_array(root, 2, 3)


def lca_recursive(root: Node, lca, node_a, node_b):
    if root is None:
        return False, lca

    if root.data == node_a or root.data == node_b:
        return True, root

    left, lca = lca_recursive(root.left, lca, node_a, node_b)
    right, lca = lca_recursive(root.right, lca, node_a, node_b)

    if left and right:
        lca = root
    return (left or right), lca


print(lca_recursive(root, None, 2, 8)[1].data)
print(lca_recursive(root, None, 2, 3)[1].data)
