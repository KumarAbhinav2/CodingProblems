class Solution:
    def runningSum(self, nums):
        r_sum = [nums[0]]
        for i in range(1, len(nums)):
            r_sum.append(nums[i] + r_sum[i - 1])
        return r_sum

obj = Solution()
obj.runningSum([1,2,3,4])
