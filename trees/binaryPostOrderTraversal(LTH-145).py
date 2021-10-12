# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        t, s = [], [(root, False)]
        while s:
            node, visited = s.pop()
            if node:
                if visited:
                    t.append(node.val)
                else:
                    s.append((node, True))
                    s.append((node.right, False))
                    s.append((node.left, False))
        return t