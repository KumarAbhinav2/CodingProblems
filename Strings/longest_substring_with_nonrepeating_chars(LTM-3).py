class Solution:
    def lengthOfLongestSubString(self, s):
        ans = 0
        mp = {}
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j-i+1)
            mp[s[j]] = j+1
        return ans

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in visited and start <= visited[c]:
                start = visited[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            visited[c] = i
        return max_length


    # Time: O(n)
    # Space: O(min(mn))

obj = Solution()
print(obj.lengthOfLongestSubString("dvdf"))