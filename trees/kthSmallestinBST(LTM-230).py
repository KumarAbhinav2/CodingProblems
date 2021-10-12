class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        res = []
        _stack = []
        while _stack or root:
            while root:
                _stack.append(root)
                root = root.left
            root = _stack.pop()
            res.append(root)
            root = root.right
        return res[k-1].val

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        def rec(root):
            if not root:return []
            else:
                return rec(root.left)+[root.val]+rec(root.right)
        res = rec(root)
        return res[k-1]

    def kthSmallest3(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -=1
            if not k:
                return root.val
            root = root.right

        # Time: O(H+k)
        # Space: O(H)



