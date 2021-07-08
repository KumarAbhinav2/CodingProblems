import heapq
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        def reachable(k):
            jumps = [y-x for y, x in zip(heights[1:k+1], heights[:k+1])]
            return len(jumps) <= ladders or sum(jumps) <= bricks

        start, end = 0, len(heights)-1
        while start < end:
            mid = (start+end)//2
            if reachable(mid):
                start = mid
            else:
                end = mid
        return start

    def furthestBuilding1(self, A, bricks, ladders):
        heap = []
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(A) - 1

obj = Solution()
obj.furthestBuilding1([4,12,2,7,3,18,20,3,19], 10, 2)

