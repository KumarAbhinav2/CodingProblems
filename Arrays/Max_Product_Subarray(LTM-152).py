class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            temp_arr = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
            min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)

            max_so_far = temp_arr

            result = max(result, max_so_far)

        return result

    # Time: O(N)
    # Space: O(1)