class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # getting the smallest string based on length, lcp driven by smallest string
        shortest = min(strs, key = len)
        for i, val in enumerate(shortest):
            # checking prefix common in rest of the strings
            for other in strs:
                if other[i] != val:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix1(self, strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

