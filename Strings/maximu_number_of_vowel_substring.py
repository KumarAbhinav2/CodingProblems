import collections
# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         max_str = ''
#         ans = cnt = 0
#         for i, c in enumerate(s):
#             if c in vowels:
#                 cnt += 1
#             if i >= k and s[i - k] in vowels:
#                 if len(s[i-k:i]) > len(max_str):
#
#         return max_str

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        curr, counts, ans = collections.deque(), 0, 0
        for a in s:
            if a in vowels:
                counts += 1
            curr.append(a)
            if len(curr) == k:
                ans = max(ans, counts)
                if curr[0] in vowels:
                    counts -= 1
                curr.popleft()
        return ans

obj = Solution()
print(obj.maxVowels('aeiouia', 3))