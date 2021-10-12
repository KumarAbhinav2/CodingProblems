# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle1(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
