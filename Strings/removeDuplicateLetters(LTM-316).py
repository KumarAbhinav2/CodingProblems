"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s):
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            # this ensures we are making the output lexicographically
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            # this ensures we are having unique elements
            if c[s[i]] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], '')) if s else ''

    # Time Complexity: O(N), each recursive call will take O(N) and there can be 26 chars which is constant
    # Space Complexity: O(N), each time we slice the string we create a new one O(N) * C(26 constant)

    def removeDuplicateLetters_Stack(self, s):
        _stack = []
        seen = set()
        # We will use this when removing elements from stack
        last_index = {v:i for i,v in enumerate(s)}

        for index, val in enumerate(s):
            if val not in seen:
                while _stack and val < _stack[-1] and index < last_index[_stack[-1]]:
                    # update both stack and set
                    seen.discard(_stack.pop())
                seen.add(val)
                _stack.append(val)
        return ''.join(_stack)

    # Time Complexity: O(N)
    # Space Complexity: O(1)
