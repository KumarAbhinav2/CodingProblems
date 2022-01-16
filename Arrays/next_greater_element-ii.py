class Solution:
    def nextGreaterElements(self, nums):
        stack = []; res = [-1]*len(nums)
        count = 0
        while count!=2:
            for i in range(len(nums)-1, -1, -1):
                if stack and nums[stack[-1]] > nums[i]:
                    res[i] = nums[stack[-1]]
                stack.append(i)
            count+=1
        print(res)

obj = Solution()
obj.nextGreaterElements([3, 8, 4, 1, 2])