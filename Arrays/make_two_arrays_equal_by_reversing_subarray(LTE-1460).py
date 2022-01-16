from collections import Counter
class Solution:

    def canBeEqual(self, target, arr):
        counter = Counter(target)
        for a in arr:
            if a not in counter or counter[a] == 0:
                return False
            counter[a]-=1
        return all((v==0 for v in counter.values()))


