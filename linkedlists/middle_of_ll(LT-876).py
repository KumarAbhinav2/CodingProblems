
class Solution:

    def smarter(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def intuitive(self, head):
        temp = []
        while head is not None:
            temp.append(head)
            head = head.next
        num = len(temp)//2
        return temp[num]


