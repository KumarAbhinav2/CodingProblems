class Solution:
    def getIntersectionNode(self, headA, headB):
        currA = headA
        currB = headB
        hmap = set()
        while currA:
            if currA not in hmap:
                hmap.add(currA)
            currA = currA.next
        while currB:
            if currB in hmap:
                return currB
            currB = currB.next
        return None

    def getIntersectionNode2(self, headA, headB):
        if not headA or not headB:
            return headA or headB
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pb is None else pa.next
            pb = headA if pa is None else pb.next
        return pa