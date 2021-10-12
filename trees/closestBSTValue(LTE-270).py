class Solution:
    def closestValue(self, root, target):
        if not root: return
        pred = float('-inf')

        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        ordered = inorder(root)

        for i in range(len(ordered)):
            if pred <= target and ordered[i] > target:
                return min(pred, ordered[i], key=lambda x: abs(target - x))
            pred = ordered[i]
        return pred

    # Time Complexity: O(H)
    # Space Complexity: O(H)


    def closestValue_better(self, root, target):
        stack = []
        pred = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred <=target and target>root.val:
                return min(pred, root.val, key = lambda x: abs(target-x))

            pred = root.val
            root = root.right

        return pred

    # Time Complexity: O(k), till you found closest i.e index of the closest element
    # Space Complexity: O(H), we have extra stack


    def closestValue_better1(self, root, target):
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target-x))
            root = root.left if target < root.val else root.right
        return closest

    # Time Complexity: O(H), can't be O(logN) as tree might not be actually balanced 
    # Space Complexity: O(1)

import heapq
class Solution:
    def closestValue(self, root, target: float) -> int:
        def rec(node):
            if not node:
                return []
            return rec(node.left) + [(abs(target - node.val), target)] + rec(node.right)

        res = rec(root)
        heapq.heapify(res)
        return res[0][0]