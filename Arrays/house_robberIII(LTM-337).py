class Solution:

    def rob(self, root):
        rob_memo = {}
        not_rob_memo = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_memo:
                    return rob_memo[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_memo[node] = result
                return result
            else:
                if node in not_rob_memo:
                    return not_rob_memo[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_memo[node] = result
                return result
        return helper(root, False)