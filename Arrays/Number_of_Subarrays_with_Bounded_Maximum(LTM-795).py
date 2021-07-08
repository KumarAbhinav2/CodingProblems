class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        L_ind, R_ind, ans = -1, -1, 0
        for i, num in enumerate(A):
            if num >= L: L_ind = i
            if num > R:  R_ind = i
            ans += L_ind - R_ind
        return ans

    def numSubarrayBoundedMax_dp(self, A, L, R):
        res, dp = 0, 0
        prev = -1
        arrs = []
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res, arrs

obj = Solution()
#print(obj.numSubarrayBoundedMax_dp([2,1,4,3], 2, 3))
print(obj.numSubarrayBoundedMax_dp([1,2,4,3], 3, 4))