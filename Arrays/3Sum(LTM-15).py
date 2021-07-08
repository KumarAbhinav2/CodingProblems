class Solution:

    def twoSum(self, nums, i, res):
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            c_sum = nums[i] + nums[lo] + nums[hi]
            if c_sum < 0:
                lo +=1
            elif c_sum > 0:
                hi -=1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo+=1
                hi-=1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo+=1

    def threeSum(self, nums):
        res = []
        nums.sort() # O(nlogn)
        for i in range(len(nums)): # O(n**2)
            if nums[i]>0:
                break
            elif i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)

    # Time: O(n**2 + nlogn) ~ O(n**2)
    # Space: O(n)