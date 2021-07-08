class Solution:

    def rob(self, nums):
        return self._rob(nums, len(nums)-1)

    def _rob(self, nums, i):
        if i < 0:
            return 0
        return max(self._rob(nums, i-2)+nums[i], self._rob(nums, i-1))


class Solution2:
    def rob(self, nums):
        self.memo = [-1]*(len(nums)+1)
        return self._rob(nums, len(nums) - 1)

    def _rob(self, nums, i):
        if i < 0:
            return 0
        if self.memo[i] >= 0:
            return self.memo[i]
        self.memo[i] = max(self._rob(nums, i-2)+nums[i], self._rob(nums, i-1))
        return self.memo[i]

class Solution3:
    def rob(self, nums):
        memo = [-1]*(len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i+1] = max(memo[i-1]+nums[i], memo[i])
        return memo[-1]


obj = Solution()
print(obj.rob([1, 2, 3, 1]))