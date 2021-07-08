from collections import Counter
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        i = 0
        res = 0
        while i+k <= len(s):
            ss = s[i:i + k]
            for j in Counter(ss).values():
                if j != 1:
                    break
            else:
                res+=1
            i+=1
        return res

obj = Solution()
print(obj.countGoodSubstrings("xyzzaz"))
print(obj.countGoodSubstrings("aababcabc"))
