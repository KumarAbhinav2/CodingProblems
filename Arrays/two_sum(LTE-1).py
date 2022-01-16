"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
"""

class Solution:

    def twoSum(self, nums, target: int):
        mmap = {}
        for i, v in enumerate(nums):
            if v in mmap:
                return [mmap[v], i]
            mmap[target-v] = i