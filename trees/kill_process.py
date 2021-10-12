class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []


class Solution:

    def killProcess(self, pid, ppid, kill: int):
        m = {}
        res = []
        for i, p in enumerate(pid):
            child_node = TreeNode(val=p)
            m[p] = child_node
        for i, p in enumerate(ppid):
            if p > 0:
                parent_node = m.get(p)
                parent_node.children.append(m.get(pid[i]))
        res.append(kill)
        self.recursive_child_check(m.get(kill), res)
        return res

    def recursive_child_check(self, node, res):
        for child in node.children:
            res.append(child)
            self.recursive_child_check(child, res)

obj = Solution()
print(obj.killProcess([1, 2, 3], [0,1 , 2], 1))