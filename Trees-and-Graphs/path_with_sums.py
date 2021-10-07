# You are given a binary tree in which each node contains an integer value
# (which might be positve or negative). Design an algorithm to count the number
#  of paths that sum to a given value. the path does not need to start or end
# at root or leaf, but it must go downwards (travelling from parent node to
# child nodes)


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
root.right.left.left = Node(-13)
root.right.left.right = Node(-13)
root.right.right = Node(8)


#                   (5)
#           (3)             (7)
#       (2)    (4)      (6)     (8)


def count_paths_with_sum(root: Node, targetSum: int):
    if root is None:
        return 0
    paths_from_root = count_paths_with_sum_from_node(root, targetSum, 0)
    paths_from_left = count_paths_with_sum(root.left, targetSum)
    paths_from_right = count_paths_with_sum(root.right, targetSum)

    return paths_from_root + paths_from_left+ paths_from_right

def count_paths_with_sum_from_node(node: Node, target_sum: int, current_sum: int):
    if node is None:
        return 0

    total_paths = 0
    current_sum += node.data
    if current_sum == target_sum:
        total_paths += 1

    total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
    total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)

    return total_paths

print(count_paths_with_sum(root, 5))
