class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            curr_score = s[:i].count('0') + s[i:].count('1')
            max_score = max(curr_score, max_score)
        return max_score

    # Time: O(n)
    # Space: O(1)