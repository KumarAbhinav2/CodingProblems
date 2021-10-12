class Solution:

    def preorder(self, root):
        if not root:
            return []

        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children[::-1])
        return output

    # Time Complexity: O(n)
    # Space Complexity: O(n)