class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        # n = len(cardPoints)
        # t_sum = sum(cardPoints)
        # ans = 0
        # for i in range(k+1):
        #     c_window = cardPoints[i:i+n-k]
        #     ans = max(ans, t_sum - sum(c_window))
        # return ans
        n = len(cardPoints)
        t_sum = sum(cardPoints)
        prev_sum = sum(cardPoints[0:n-k])
        ans = t_sum - prev_sum
        for i in range(1,k+1):
            c_sum = prev_sum - cardPoints[i-1]+cardPoints[n-k-1+i]
            ans = max(ans, t_sum - c_sum)
            prev_sum = c_sum
        return ans


obj = Solution()
print(obj.maxScore([1,2,3,4,5,6,1], 3))
print(obj.maxScore([9,7,7,9,7,7,9], 7))
print(obj.maxScore([1,1000,1], 1))
print(obj.maxScore([1,79,80,1,1,1,200,1], 3))
print(obj.maxScore([2,2,2], 2))
print(obj.maxScore([96,90,41,82,39,74,64,50,30],8))