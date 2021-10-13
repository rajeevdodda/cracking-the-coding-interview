# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def validate(self, root, low, high):
        if root is None:
            return True
        else:
            if root.left and root.left.val >= root.val:
                return False
            elif root.right and root.right.val <= root.val:
                return False
            elif not low < root.val < high:
                return False
            return self.validate(root.left, low, root.val) and self.validate(
                root.right, root.val, high
            )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
