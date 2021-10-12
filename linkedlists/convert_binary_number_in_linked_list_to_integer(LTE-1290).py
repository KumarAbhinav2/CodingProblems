class Solution:

    def getDecimalValue(self, head):
        curr = head
        ll = 0
        while curr:
            curr = curr.next
            ll += 1
        curr = head
        p = ll - 1
        num = 0
        while curr:
            num += 2 ** p * curr.val
            curr = curr.next
            p -= 1
        return num

    def getDecimalValue2(self, head):
        curr = head
        num = curr.val
        while curr:
            num = num*2+curr.next.val
            curr = curr.next
        return num

    # Time: O(n)
    # Space: O(1)