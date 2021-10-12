class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthNode(self, head, n):
        # Taking a dummy node to point to head
        dummy = ListNode()
        # Both slow and fast pointers will start from dummy pointer
        slow = fast = dummy
        dummy.next = head
        # move fast to n steps ahead
        for _ in range(n):
            fast = fast.next
        # while fast reaches end, slow will be 1 node behind the nth node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        # return before head
        return dummy.next

class Solution2:
    def removeNthNode(self, head, n):
        dummy = ListNode()
        dummy.next = head
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l+=1
        l -=n
        curr = dummy
        while l > 0:
            curr = curr.next
            l-=1
        curr.next = curr.next.next
        return dummy.next

    # Time: O(L)
    # Space: O(1)
