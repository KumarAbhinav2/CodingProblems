class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        j = n
        i = 0
        while i < len(s):
            left_s = s[i:j]
            if left_s == part:
                s = s[:i]+s[j:]
                i=0;j=n
            else:
                j+=1;i+=1
        return s

obj = Solution()
print(obj.removeOccurrences("daabcbaabcbc", "abc"))
print(obj.removeOccurrences("axxxxyyyyb", "xy"))