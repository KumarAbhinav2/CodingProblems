class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0; j = len(nums) - 1
        pairs = []
        while i < j:
            pairs.append(nums[i], nums[j])
        arr = [sum(x) for x in pairs]
        return max(arr)
