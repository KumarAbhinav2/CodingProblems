from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums):
        map = Counter(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in map:
                res.append(i)
        return res





    def findDisappearedNumbers_better(self, nums):
        res = []
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1

            if nums[new_index] > 0:
                nums[new_index] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)


