"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""

class Solution:

    def restoreString(self, s: str, indices) -> str:
        res = ['']*len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(res)

    def restoreString2(self, s: str, i) -> str:
        return ''.join([i[0] for i in sorted(zip(s, i), key=lambda x:x[1])])
