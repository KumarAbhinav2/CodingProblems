from collections import Counter
class Solution:
    def largestUniqueNumber(self, A):
        mmp = Counter(A)
        res = sorted([k for k,v in mmp.items() if v==1], reverse=True)
        return res[0] if res else -1

    # Time: O(n)
    # Space: O(n)


obj = Solution()
print(obj.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))