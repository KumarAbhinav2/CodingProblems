class Solution:

    def numIdenticalPairs(self, nums) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        res = 0
        for i in nums:
            dp[i]+=1
        for v in dp.values():
            res += (v*(v-1))//2
        return res

obj = Solution()
print(obj.numIdenticalPairs([1,2,3,1,1,3]))
print(obj.numIdenticalPairs([1,1,1,1]))