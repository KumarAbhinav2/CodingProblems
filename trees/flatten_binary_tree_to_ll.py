# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def rec(root):
            if not root:
                return []

            return [root.val] + rec(root.left) + rec(root.right)

        res = rec(root)





