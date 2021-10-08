# https://www.techiedelight.com/count-nodes-bst-that-lies-within-given-range/

# Count nodes in a BST that lies within a given range

from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()

for i in range(1, 10):
    bst.insert(i)


def count_nodes(root, min_value, max_value):
    if root is None:
        return 0

    count = 0

    if min_value < root.data < max_value:
        count += 1

    count = count + count_nodes(root.left, min_value, max_value)
    count = count + count_nodes(root.right, min_value, max_value)

    return count


bst.inorder(bst.root)
print()
print(count_nodes(bst.root, 5, 10))
print(count_nodes(bst.root, 11, 12))
