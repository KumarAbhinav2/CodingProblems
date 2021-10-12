
class Solution:

    def searchBST(self, root, val):
        if not root:
            return
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        return root

    # Time Complexity: O(n)
    # Space Complexity: O(n) - recursion stack

    def searchBST(self, root, val):
        while root is not None and root.val != val:
            root = root.left if root.val > val else root.right
        return root
    # Time Complexity: O(n), O(logN) average case
    # Space Complexity: O(1)