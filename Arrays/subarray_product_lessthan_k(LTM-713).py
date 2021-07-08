class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1: return 0

        left = ans = 0

        prod = 1

        for right, val in enumerate(nums):
            prod *= val

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right - left + 1
        return ans

    # Time: O(n)
    # Space: O(1)

obj = Solution()
obj.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
