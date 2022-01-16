class Solution:
    def maxScore1(self, s: str) -> int:
        j = 1
        max_sum = 0
        while j < len(s):
            left, right = s[:j].count('0'), s[j:].count('1')
            print(s[:j], '--', s[j:])
            max_sum = max(max_sum, left + right)
            j += 1
        return max_sum

    '''a, b = 0, s[1:].count('1')
    ans = b
    if s[0] == '1':
        b += 1
    for c in s[0:-1]:
        if c == '0':
            a += 1
        elif c == '1':
            b -= 1
        ans = max(ans, a + b)
    return ans'''

    def maxScore(self, s: str) -> int:
        a, b = 0, s[1:].count('1')
        ans = b
        if s[0] == '1':
            b += 1
        for c in s[0:-1]:
            if c == '0':
                a += 1
            elif c == '1':
                b -= 1
            ans = max(ans, a + b)
        return ans

print(Solution().maxScore("011101"))