# T1 and T2 are two very large binary trees, with T1 much bigger thab T2.
# Create an algorithm to determine if T2 is a subtree of T1.


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


tree_1 = Node("1")

tree_1.left = Node("2")
tree_1.right = Node("3")

tree_1.left.left = Node("4")

tree_1.right.left = Node("6")
tree_1.right.right = Node("7")


#             (1)
#     (2)             (3)
# (4)            (6)     (7)


tree_2 = Node("3")

tree_2.left = Node("6")
tree_2.right = Node("7")
tree_2.right.left = Node("7")


def get_nodes_string(tree: Node, stack: list):
    if not tree:
        stack.append("X")
        return
    stack.append(tree.data)
    get_nodes_string(tree.left, stack)
    get_nodes_string(tree.right, stack)
    return stack


def check_sub_tree(tree_1: Node, tree_2: Node):
    tree_1_string = "".join(get_nodes_string(tree_1, []))
    tree_2_string = "".join(get_nodes_string(tree_2, []))
    print(tree_1_string, tree_2_string)

    for i in range(len(tree_1_string)):
        if tree_1_string[i : i + len(tree_2_string)] == tree_2_string:
            print(True)
            break
    else:
        print(False)


check_sub_tree(tree_1, tree_2)


def check_sub_tree_recursive(tree_1: Node, tree_2: Node):
    if tree_2 is None:
        return True
    else:
        return sub_tree_helper(tree_1, tree_2)


def sub_tree_helper(tree_1: Node, tree_2: Node):
    if tree_1 is None:
        return False
    elif tree_1.data == tree_2.data and match_tree(tree_1, tree_2):
        return False
    return sub_tree_helper(tree_1.left, tree_2) or sub_tree_helper(tree_1.right, tree_2)


def match_tree(tree_1: Node, tree_2: Node):

    if tree_2 is None and tree_1 is None:
        return True
    elif tree_1 is None or tree_2 is None:
        return False
    elif tree_1.data != tree_2.data:
        return False
    else:
        return match_tree(tree_1.left, tree_2.left) and match_tree(
            tree_1.right, tree_2.right
        )

print(check_sub_tree_recursive(tree_1, tree_2))