import heapq
class Solution:
    def maxNumberOfApples(self, nums):
        nums.sort()
        apples = units = 0
        for _, w in enumerate(nums):
            units+=w
            if units > 5000:
                break
            apples+=1
        return apples

    # Time: O(N)
    # Space: O(N)


    def maxNumberOfApples_better(self, nums):
        heapq.heapify(nums)
        apples = 0
        units = 0
        while nums and units+nums[0] < 5000:
            units += heapq.heappop(nums)
            apples+=1
        return apples

    # Time: O(N+logK) N for heapify and logK while heappop
    # Space: O(N)