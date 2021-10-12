class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = Node(cur.val)
            #dic[cur].random = cur.random
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]

head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
obj = Solution()
obj.copyRandomList(head)