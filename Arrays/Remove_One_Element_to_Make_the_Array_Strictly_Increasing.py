class Solution2:
    def canBeIncreasing(self, nums) -> bool:
        count = 0
        if nums[0] > nums[1]:
            count+=1
        for i in range(1, len(nums)-1):
            if (nums[i-1] < nums[i] and nums[i] > nums[i+1]) or (nums[i-1] > nums[i] and nums[i] < nums[i+1]):
                if nums[i] == nums[i-1] or nums[i] ==nums[i+1]:
                    return False
                count+=1
                nums[i] = nums[i - 1]
        if nums[len(nums)-1] == nums[len(nums)-2]:
            return False
        if count > 1:
            return False
        return True


class Solution:
    def canBeIncreasing2(self, nums) -> bool:
        removed_one = False
        prev_max = None
        max_total = None
        for num in nums:
            if not maxval or s > maxval:
                prev_maxval = maxval
                maxval = s
            elif not prev_maxval or s > prev_maxval:
                if removed_one:
                    return False
                removed_one = True
                maxval = s
            else:
                if removed_one:
                    return False
                removed_one = True
        return True

    def canBeIncreasing(self, nums):
        indexes = []

        for i, v in enumerate(nums):
            tmp = []
            for j in range(i - 1, -1, -1):
                if nums[i] <= nums[j]:
                    tmp.append(j)
            if len(tmp) > 1:
                indexes.append(i)
            else:
                if len(tmp) > 0:
                    indexes.append(tmp[0])
        return len(set(indexes)) <= 1


obj = Solution()
print(obj.canBeIncreasing([1,2,10,5,7]))
print(obj.canBeIncreasing([2,3,1,2]))
print(obj.canBeIncreasing([1,1,1]))
print(obj.canBeIncreasing([1,2,3]))
print(obj.canBeIncreasing([1,1]))


