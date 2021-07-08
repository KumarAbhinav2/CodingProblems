class Solution:
    def moveZeroes(self, nums):
        count = nums.count(0)
        nums[:] = [i for i in nums if not i]
        nums += [0]*count