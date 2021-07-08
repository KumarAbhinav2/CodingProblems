"""
Check how many arithmetic subarrays of length atleast 3 is possible from given array

input = [1,2, 3, 4]
output = 3
"""


class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        dp = 0
        res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res

    def numberOfArithmeticSlices2(self, nums) -> int:
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1]
        return sum(dp)

obj = Solution()
#print(obj.numberOfArithmeticSlices([1, 2, 3,4]))
print(obj.numberOfArithmeticSlices([1,2,3,8,9,10]))