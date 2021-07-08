class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def _rob(nums):
            memo = [-1] * (len(nums) + 1)

            memo[0] = 0
            memo[1] = nums[0]
            for i in range(1, len(nums)):
                memo[i + 1] = max(memo[i - 1] + nums[i], memo[i])
            return memo[-1]

        return max(_rob(nums[1:]), _rob(nums[:len(nums) - 1]))


obj = Solution()
obj.rob([0])