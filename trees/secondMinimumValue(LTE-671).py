class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findSecondMinimumValue(self, root) -> int:
        def minimum(root):
            mini = float('inf')
            if root.right and root.right.val!=root.val:
                mini = min(mini,root.right.val)
            if root.left and root.left.val!=root.val:
                mini = min(mini,root.left.val)
            if root.right:
                mini =  min(mini,minimum(root.right))
            if root.left:
                mini =  min(mini, minimum(root.left))
            return mini

        res = minimum(root)
        if res==float('inf'):
            return -1
        return res

    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        def rec(root):
            if not root: return []
            else:
                return rec(root.left)+[root.val]+rec(root.right)
        res = set(rec(root))
        if len(res)>=2:
            return sorted(list(res))[1]
        else:
            return -1
