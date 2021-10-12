# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            root1.val+=root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        else:
            return root1 or root2

    def mergeTrees2(self, root1: TreeNode, root2: TreeNode):
        if not root1:
            return root2
        stack = []
        stack.append((root1, root2))
        while stack:
            t = stack.pop()
            if not t[0] or not t[1]:
                continue
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return root1


    # Time: O(n)
    # Space: O(n)