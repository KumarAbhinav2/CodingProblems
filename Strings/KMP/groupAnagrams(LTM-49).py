from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for a in strs:
            sa = ''.join(sorted(a))
            res[sa].append(a)
        return [a for a in res.values()]


obj = Solution()
obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"])