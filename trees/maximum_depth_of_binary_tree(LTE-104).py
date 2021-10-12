# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        _stack = [(1, root)]
        depth = 0
        while _stack:
            curr_depth, node = _stack.pop()
            if node:
                depth = max(curr_depth, depth)
                _stack.append((curr_depth+1, node.left))
                _stack.append((curr_depth+1, node.right))
        return depth

    # Time: O(N)
    # Space: O(N)