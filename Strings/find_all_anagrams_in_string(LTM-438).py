from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        np = len(p)
        ns = len(s)
        if ns < np:
            return []
        p_count = Counter(p)
        s_count = Counter()
        res = []
        for i in range(ns):
            s_count[s[i]]+=1
            if i >= len(p):
                if s_count[s[i-np]] == 1:
                    del s_count[s[i-np]]
                else:
                    s_count[s[i-np]] -=1
            if p_count == s_count:
                res.append(i-np+1)
        return res

    # Time: O(N)  # N = Ns+Np
    # Space: O(1)  # 26 chars only
