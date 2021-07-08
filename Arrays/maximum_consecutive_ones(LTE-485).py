class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_sum = 0
        curr_max = 0
        for i in nums:
            if i:
                curr_max += i
                max_sum = max(curr_max, max_sum)
            else:
                curr_max = 0
        return max_sum

    # Time: O(N)
    # Space: O(1)
