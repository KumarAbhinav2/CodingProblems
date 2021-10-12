class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next_node = next

class Solution:

    def oddEvenList(self, head):
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next_node = head
                odds = odds.next_node
            else:
                evens.next_node = head
                evens = evens.next_node
            isOdd = not isOdd
            head = head.next_node
        evens.next_node = None
        odds.next = evensHead.next_node
        return oddsHead.next_node

    def oddEvenList2(self, head: ListNode) -> ListNode:
        if not head: return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

obj = Solution()

from linkedlist import LinkedList
o = LinkedList()
for i in [5, 4, 3, 2, 1]:
    o.insert_at_head(i)

o.print_list()
head= o.get_head()
obj.oddEvenList(head)