# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low: int, high: int):
        def rec(node):
            if not node:
                return
            elif node.val < low:
                # all value should be anyways less than low(BST property) so we have to discard it
                return rec(node.right)
            elif node.val > high:
                # all values in right subtree will not be in the range so better discard it
                return rec(node.left)
            else:
                # we might have to trim both side of root
                node.left = rec(node.left)
                node.right = rec(node.right)
                return node
        return rec(root)

    # Time: O(N)   # N total number of nodes
    # Space: O(N)  # recursion stack