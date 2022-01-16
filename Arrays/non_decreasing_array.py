class Solution:
    def checkPossibility(self, nums) -> bool:
        count=1
        max_count = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
            i += 1
        diff = len(nums) - max_count
        if diff > 1:
            return False
        return True


obj = Solution()
# print(obj.checkPossibility([4,2,3]))
# print(obj.checkPossibility([4,2,1]))
print(obj.checkPossibility([3,4,2,3]))

