class Solution:
    def findMaxConsecutiveOnes_bf(self, nums) -> int:
        longest_sequence = 0
        for i in range(len(nums)):
            num_zeroes = 0
            for j in range(i, len(nums)):
                if num_zeroes == 2:
                    break
                if nums[j] == 0:
                    num_zeroes+=1
                if num_zeroes <= 1:
                    longest_sequence = max(longest_sequence, j-i+1)
        return longest_sequence

        # Time: O(n**2)
        # Space: O(1)

    def findMaxConsecutiveOnes_slidingWindow(self, nums):
        left, right = 0,0
        longest_sequence = 0
        num_zeroes = 0
        while right < len(nums):
            if nums[right] == 0:
                num_zeroes +=1
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes-=1
                left+=1
            longest_sequence = max(longest_sequence, right-left+1)
            right+=1
        return longest_sequence

        # Time: O(N)
        # Space: O(1)
