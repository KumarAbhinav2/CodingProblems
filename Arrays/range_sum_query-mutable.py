from itertools import accumulate
from operator import add

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums):
        def buildTree(nums, l, r):
            if l>r:
                return
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l+r)//2
            root = Node(l,r)
            root.left = buildTree(nums, l, mid)
            root.right = buildTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = buildTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start+root.end)//2
            if i <= mid:
                updateVal(root.left,i,val)
            else:
                updateVal(root.right, i, val)
            root.total = root.left.total+root.right.total
            return root.total
        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        pass

numArray = NumArray([1, 3, 5])
numArray.sumRange(0, 2)# return 1 + 3 + 5 = 9
numArray.update(1, 2)# nums = [1, 2, 5]
numArray.sumRange(0, 2)# return 1 + 2 + 5 = 8