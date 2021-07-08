class Solution:

    def __is_interleave(self, s1, i, s2, j, res, s3):
        if res == s3 and i == len(s1) and j == len(s2):
            return True
        ans = False
        if i < len(s1):
            ans |= self.__is_interleave(s1, i+1, s2, j, res+s1[i], s3)
        if j < len(s2):
            ans |= self.__is_interleave(s1, i, s2, j+1, res+s2[j], s3)
        return ans

    def isInterleave(self, s1: str, s2: str, s3: str):
        if len(s1)+len(s2) != len(s3):
            return False
        return self.__is_interleave(s1, 0, s2, 0, '', s3)




obj = Solution()
print(obj.isInterleave("abc", "bcd", "abcbdc"))
