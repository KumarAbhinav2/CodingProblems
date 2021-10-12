class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        # If root found none, return newly created Node
        if not root: return TreeNode(val)
        # checking if the value belongs to left subtree or right subtree
        if val < root.val:
            # recursively call method with reference to left sub tree
            # no need to check if left child exists or not as this will handled in base case
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # Time Complexity: O(H), where H is the height of the Tree
    # Space Complexity: O(n), For maintaining recursive stack

    def insertIntoBST_Iterative(self, root, val):
        node = root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
        return TreeNode(val)

    # Time Complexity: O(H)
    # Space Complexity: O(1)



    "str".translate()