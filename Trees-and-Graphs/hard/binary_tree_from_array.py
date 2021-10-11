# https://www.techiedelight.com/build-binary-tree-given-parent-array/

# Build a binary tree from a parent array


parent_arrray = [-1, 0, 0, 1, 2, 2, 4, 4]

elements = ["a", "b", "c", "d", "e", "f", "g"]


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_binary_tree(parent: list, elements: list):
    hash_map = {}

    for i in range(len(parent)):
        hash_map[i] = Node(elements[i])
    root = None
    for i in parent:
        if i == -1:
            root = hash_map[0]
        else:
            parent_node = hash_map[i]
            if parent_node.left:
                parent_node.right = None

