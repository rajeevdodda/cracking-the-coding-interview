#  https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        all_paths = []
        self.get_path(root, path, all_paths)
        ans = 0
        for i in all_paths:
            ans += int(i)
        return ans

    def get_path(self, root, path, all_paths):
        if root is None:
            return
        path.append(str(root.val))
        self.get_path(root.left, path, all_paths)
        if root.left is None and root.right is None:
            all_paths.append("".join(path))
        self.get_path(root.right, path, all_paths)
        path.pop()
