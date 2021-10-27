# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        for i in preorder[1:]:
            self.insert(root, i)
        return root

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root
