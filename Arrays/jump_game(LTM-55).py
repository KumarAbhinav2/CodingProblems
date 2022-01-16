class Solution:

    def canJump(self, nums) -> bool:
        lastGoodPos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastGoodPos:
                lastGoodPos = i
        return lastGoodPos == 0

    # Time: O(n)
    # Space: O(1)

obj = Solution()
#obj.canJump([2,3,1,1,4])
obj.canJump([3,2,1,0,4])
