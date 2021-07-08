class Solution:

    def longestPalindrome(self, s):
        res= ''
        for c in range(len(s)):
            temp_str = self.getPalindrome(s, c, c)
            if len(temp_str) > len(res):
                res = temp_str

            temp_str = self.getPalindrome(s, c, c+1)
            if len(temp_str) > len(res):
                res = temp_str
        return res

    def getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1:right]


obj = Solution()
obj.longestPalindrome('abba')

