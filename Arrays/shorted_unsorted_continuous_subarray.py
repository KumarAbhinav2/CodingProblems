class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        s_nums = sorted(nums)
        l = []
        for i, (x, y) in enumerate(zip(nums, s_nums)):
            if x != y:
                l.append(i)
        return len(nums[l[0]:l[-1]+1])

obj = Solution()
print(obj.findUnsortedSubarray([2,6,4,9,15]))