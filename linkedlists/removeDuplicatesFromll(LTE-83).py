
class Solution:

    def removeDuplicates_set(self, head):
        seen = set()
        curr = head
        prev = None
        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next
        return head

        # Time Complexity: O(n)
        # Space Complexity: O(n)

    def removeDuplicates_inplace(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

        # Time Complexity: O(n)
        # Space Complexity: O(1)
