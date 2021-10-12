# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head: return False
        mlist = []
        curr = head
        while curr:
            mlist.append(curr.val)
            curr = curr.next
        return mlist == mlist[::-1]

    # Time: O(n)
    # Space: O(n)

    def isPalindrome2(self, head) -> bool:
        if not head:
            return True

        first_half = self.get_middle(head)
        second_half = self.reverse_list(first_half.next)
        curr = head
        sec = second_half
        result = True
        while result and sec:
            if curr.val != sec.val:
                result = False
            curr = curr.next
            sec = sec.next
        return result


    def get_middle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def reverse_list(self, node):
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev



