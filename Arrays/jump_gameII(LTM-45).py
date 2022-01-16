class Solution:
    def jump(self, nums):
        j = 0
        curr_jumpend = 0
        farthest_jump = 0
        for i in range(len(nums)-1):
            farthest_jump = max(farthest_jump, i+nums[i])
            if i == curr_jumpend:
                j+=1
                curr_jumpend = farthest_jump
        return j

obj  =Solution()
print(obj.jump([2,3,1,1,4]))





