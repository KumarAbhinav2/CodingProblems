from collections import Counter
class Solution:

    def numJewelsInStones(self, j, s):
        return sum(map(s.count, j))

    def numJewelsInStones2(self, j, s):
        st_count = Counter(s)
        return sum([st_count.get(j, 0) for j in set(j)])

