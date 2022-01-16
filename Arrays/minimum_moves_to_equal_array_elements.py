class Solution:
    def minMoves2(self, nums):
        nums.sort()
        i = 0; j = len(nums)-1
        target = (i + j) // 2
        return sum([abs(n-nums[target]) for n in nums])

obj = Solution()
print(obj.minMoves2([1,2,3]))
print(obj.minMoves2([1,10,2,9]))

