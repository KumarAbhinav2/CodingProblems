from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust) -> int:
        labels = set(range(1, N+1))
        counts = defaultdict(int)
        for i in trust:
            if i[0] in labels:
                labels.remove(i[0])
            counts[i[1]] += 1
        if not labels:
            return -1
        judge = labels.pop()
        if counts[judge] == N - 1:
            return judge
        return -1

obj = Solution()
obj.findJudge(3, [[1,2],[2,3]])

