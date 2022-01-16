from collections import Counter
class Solution:
    def findShortestSubArray(self, nums) -> int:
        counts = Counter(nums)
        org_fre = sorted(counts.values())[-1]
        interested_elem = [i for i,v in counts.items() if v == org_fre]
        min_len = float('inf')
        for j in interested_elem:
            min_arr = []
            for i in range(len(nums)):
                if nums[i] == j:
                    min_arr.append(i)
            min_len = min(min_len, len(nums[min_arr[0]:min_arr[-1]+1]))
        return min_len

obj = Solution()
print(obj.findShortestSubArray([1, 2, 2, 3, 1]))
print(obj.findShortestSubArray([1,2,2,3,1,4,2]))
print(obj.findShortestSubArray([6,5,5]))