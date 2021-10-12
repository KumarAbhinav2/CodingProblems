class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def increasingBST(self, root):

        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)

        # we can take it as head node
        ans = cur = TreeNode(None)
        # need not stop after getting the inorder traversal
        # we need to create another tree as per the question
        for val in inorder(root):
            cur.right = TreeNode(val)
            cur = cur.right
        return ans.right

    def increasingBST2(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for val in inorder(root):
            cur.right = TreeNode(val)
            cur = cur.right
        return ans.right