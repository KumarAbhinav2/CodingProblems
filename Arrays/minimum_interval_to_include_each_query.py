import heapq
class Solution:
    def minInterval(self, intervals, queries):
        intervals = sorted(intervals, key=lambda x:abs(x[0]-x[1]))
        ans = []
        for i in queries:
            heap = []
            for j in intervals:
                if j[0]<=i<=j[1]:
                    diff = j[1]-j[0]+1
                    heapq.heappush(heap, [diff, j])
            if heap:
                diff, j = heapq.heappop(heap)
                ans.append(diff)
            else:
                ans.append(-1)
        return ans

    def minInterval_working(self, A, queries):
        A = sorted(A)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]

obj = Solution()
print(obj.minInterval_working([[1,4],[2,4],[3,6],[4,4]], [2, 3, 4, 5]))
#print(obj.minInterval_working([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))