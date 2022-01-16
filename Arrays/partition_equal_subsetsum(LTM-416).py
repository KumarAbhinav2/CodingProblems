class Solution:
    def canPartition_brute_force(self, nums) -> bool:
        memo = set([0])
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        for i in nums:
            c_memo = memo.copy()
            for s in c_memo:
                memo.add(i+s)
        return target in memo

    def canPartition_tree(self, nums):
        nums.sort(reverse=True)
        if sum(nums)%2:
            return False
        target = sum(nums)//2

        def backtrack(rem, index):
            if index >= len(nums) or rem < nums[index]:
                return False
            return backtrack(rem - nums[index], index+1) or backtrack(rem, index+1)
        backtrack(target, 0)


obj = Solution()
#print(obj.canPartition_tree([1, 2, 3, 5]))
print(obj.canPartition_tree([1, 5, 11, 5]))
# print(obj.canPartition_tree([2, 8, 3, 1]))



