class Solution:
    def minStartValue(self, nums) -> int:
        start_val = float('inf')
        step_val = 0
        for num in nums:
            step_val = step_val + num
            start_val = min(start_val, step_val)

        if start_val < 0:
            return abs(start_val) + 1
        return 1

    # Time: O(n)
    # Space: O(1)