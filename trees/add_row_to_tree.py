"""
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        q, res = [(root, 0)], []
        while q:
            node, level = q.pop()
            if level < level+1 and level+1 == d:
                res.append([])
                left_sub_tree, right_sub_tree = root.left, root.right
            res[level].append()
            q.append((root.left, level+1))
            q.append((root.right, level+1))


