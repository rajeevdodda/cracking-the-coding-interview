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


root.right.left = Node(6)
root.right.right = Node(7)


#             (1)
#     (2)             (3)
# (4)    (5)      (6)     (7)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="->")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end="->")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="->")

if __name__ == "__main__":
    print("Inorder traversal")
    inorder(root=root)

    print("\npreorder traversal")
    preorder(root=root)

    print("\npostorder traversal")
    postorder(root=root)
