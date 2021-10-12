class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        # Initialising two pointers
        right = right_head = ListNode()
        left = left_head = ListNode()
        while head:
            if head.val < x:
                # updating left pointer
                left.next = ListNode(head.val)
                left = left.next
            else:
                # updating right pointer
                right.next = ListNode(head.val)
                right = right.next
            head = head.next
        # merging the lists
        left.next = right_head.next
        return left_head.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)

