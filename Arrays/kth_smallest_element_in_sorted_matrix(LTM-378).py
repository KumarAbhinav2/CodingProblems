import heapq
class Solution:

    def kthSmallest(self, matrix, k):
        vals = []
        for row in matrix:
            vals.extend(row)
        heapq.heapify(vals)
        for _ in range(k):
            res = heapq.heappop(vals)
        return res

obj = Solution()
print(obj.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))