class Solution:
    def findLHS(self, nums) -> int:
        result = 0
        i=0;j=i+1
        nums.sort()
        while i<j and j<len(nums):
            arr = nums[i:j+1]
            diff = max(arr)-min(arr)
            if diff == 1:
                j+=1
                curr_result = len(arr)
                result = max(result, curr_result)
            else:
                i+=1
                j+=1
        return result

obj = Solution()
#print(obj.findLHS([1,3,2,2,5,2,3,7]))
print(obj.findLHS([1, 2, 2, 1]))