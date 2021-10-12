# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        pre_head = ListNode(-1)
        pre_head.next = head

        current_node = pre_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return pre_head.next

    def removeElements2(self, head, val):
        sentinel = ListNode(-1)
        sentinel.next = head

        pre, curr = sentinel, head
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        return sentinel.next

    # Time: O(N)
    # Space: O(1)


