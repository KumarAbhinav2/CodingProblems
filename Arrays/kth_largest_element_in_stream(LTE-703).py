import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        if len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif self.pool[0] < val:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
