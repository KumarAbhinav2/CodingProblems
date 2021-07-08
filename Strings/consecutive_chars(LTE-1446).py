class Solution:

    def maxPower(self, s: str) -> int:
        max_len = 0
        cur_max = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_max += 1
            else:
                cur_max = 1
            max_len = max(cur_max, max_len)
        return max_len

    # Time: O(n)
    # Space: O(1)

obj = Solution()
obj.maxPower("abbcccddddeeeeedcba")