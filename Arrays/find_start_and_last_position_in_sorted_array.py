from collections import defaultdict
class Solution:
    def searchRange(self, nums, target: int):
        i, j = 0, len(nums)-1
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.insert(0, i)
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                res.append(j)
                break
        if not res:
            return [-1, -1]
        return res

class Solution1:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]

        def bisect_lr(nums, target):
            i, j = 0, len(nums) - 1
            while i < j:
                mid = (i + j) // 2
                if nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i if nums[i] == target else -1

        def bisect_rl(nums, target):
            i, j = 0, len(nums) - 1
            while i < j:
                mid = (i + j) // 2 + 1
                if nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid
            return i if nums[i] == target else -1

        return [bisect_lr(nums, target), bisect_rl(nums, target)]

    # Time: O(logn)
    # Space: O(1)

obj = Solution()
print(obj.searchRange1([3,3,3], 3))