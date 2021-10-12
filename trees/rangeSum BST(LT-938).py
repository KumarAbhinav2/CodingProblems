

from tree import BST

class Solution:

    def rangeSumBST(self, node, L, R):
        if not node:return 0
        if node.val < L: self.rangeSumBST(node.right_child, L, R)
        if node.val > R: self.rangeSumBST(node.left_child, L, R)
        return node.val + self.rangeSumBST(node.left_child, L, R) + self.rangeSumBST(node.right_child, L, R)

obj = Solution()
t = BST()
for i in [10,5,15,3,7,18]:
    t.insert_node(i)
#print(t.root.val)
print(obj.rangeSumBST(t.root, 7, 15))
#obj.rangeSumBST([10,5,15,3,7,None,18], 7, 15)


