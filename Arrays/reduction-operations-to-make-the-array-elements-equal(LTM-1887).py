class Solution:
    def reductionOperations(self, nums) -> int:
        ans = val = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]: val += 1
            ans += val
        return ans

obj = Solution()
obj.reductionOperations([5,1,3])