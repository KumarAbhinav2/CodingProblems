class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDiffInBST1(self, root: TreeNode) -> int:
        # morris inorder traversal
        res = []
        curr = root
        min_val = float('inf')
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right
        return min(abs(res[i+1]-res[i]) for i in range(len(res)-1))

    def minDiffInBST2(self, root: TreeNode) -> int:
        if not root:
            return None
        res = []
        self.inorder(root, res)
        return min(res[i + 1] - res[i] for i in range(len(res) - 1))

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)