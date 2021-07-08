class Solution:

    def diff(self, i):
        return abs(i[0] - i[1])

    def shortestToChar(self, s: str, c: str):
        res = []
        ind_c = [i for i, x in enumerate(s) if x == c]
        for i, val in enumerate(s):
            zipped = zip(ind_c, [i] * len(ind_c))
            new_diff = min(map(self.diff, zipped))
            res.append(new_diff)
        return res