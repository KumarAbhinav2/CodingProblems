

class Solution:

    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

    def isValidBST_iterative(self, root):
        if not root: return True
        _stack = [(root, -float('inf'), float('inf'))]
        while _stack:
            node, l, r = _stack.pop()
            if node.val <= l or node.val >= r: return False
            if node.left_child: _stack.append((node.left_child, l, node.val))
            if node.right_child: _stack.append((node.right_child, node.val, r))
        return True

    def isValidBST_recursive(self, root):
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left_child, left, node.val) and rec(node.right_child, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf') )


obj = Solution()
obj.isValidBST()