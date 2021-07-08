class Solution:
    def hasAllCodes1(self, s: str, k: int) -> bool:
        substrings = set()
        for i in range(len(s)):
            if len(s[i:i+k]) == k:
                substrings.add(s[i:i+k])
        return len(substrings) == 2**k

    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        substrings = set()
        for i in range(k, len(s)+1):
            ss = s[i-k:i]
            if ss not in substrings:
                substrings.add(ss)
                need -=1
                if need == 0:
                    return True
        return False






obj = Solution()
#print(obj.hasAllCodes('00110110', 2))
#print(obj.hasAllCodes('0110', 2))
print(obj.hasAllCodes('1011100', 3))