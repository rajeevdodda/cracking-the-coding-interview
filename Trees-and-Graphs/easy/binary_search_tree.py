# Binay Search Tree


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end="->")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end="->")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end="->")


if __name__ == "__main__":
    bst = BinarySearchTree()

    #           (5)
    #     (3)         (7)
    # (2)    (4)  (6)     (8)

    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)

    print("Inorder traversal")
    bst.inorder(bst.root) # 2->3->4->5->6->7->8->

    print("\nPreorder traversal")
    bst.preorder(bst.root) # 5->3->2->4->7->6->8->

    print("\nPostorder traversal")
    bst.postorder(bst.root) # 2->4->3->6->8->7->5->
