class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedListToBST(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def rec(arr, start, end):
            if not arr: return None
            if start <= end:
                mid = (start+end)//2
                node = TreeNode(arr[mid])
                node.left = rec(arr, start, mid-1)
                node.right = rec(arr, mid+1, end)
                return node
            return rec(arr, 0, len(arr)-1)


    def sortedListToBST2(self, head):
        if not head:
            return None
        mid = self.get_middle_node(head)
        root = TreeNode(mid.val)
        if head == mid:
            return root
        root.left = self.sortedListToBST2(head)
        root.right = self.sortedListToBST2(mid.next)
        return root

    def get_middle_node(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev:
            prev.next = None
        return slow
