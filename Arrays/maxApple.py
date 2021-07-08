class Solution:
    def maxNumberOfApples(self, arr) -> int:
        if sum(arr) < 5000:
            return len(arr)
        res = 0
        apples = 0
        arr.sort()
        for i in range(len(arr)):
            if res+arr[i] <=5000:
                res+=arr[i]
                apples+=1
        return apples


obj = Solution()
print(obj.maxNumberOfApples([900,950,800,1000,700,800]))

import heapq
heapq.heappush([1, 3, 4, 5])