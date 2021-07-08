class Solution:
    def shortestSuperstring(self, words) -> str:
        comb = ''.join(words)
        comb = sorted(comb)
        for w in words:
            w_c = comb.count(w)
            if w_c > 1:
                comb = comb.replace(w, '', w_c-1)
        return comb


obj = Solution()
print(obj.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]))