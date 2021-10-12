import collections

from collections import defaultdict
class Solution:

    def countComponents_dfs(self, n: int, edges) -> int:
        visited = set()
        graph = defaultdict(list)
        count = 0
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node):
            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count


    def countComponents_bfs(self, n: int, edges) -> int:
        visited = set()
        graph = defaultdict(list)
        count = 0
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node):
            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v)

        for i in range(n):
            q = [i]
            
            if i not in visited:
                dfs(i)
                count+=1

obj = Solution()
print(obj.countComponents(5, [[0,1],[1,2],[3,4]]))
# print(obj.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))
# print(obj.countComponents(5, [[0],[1],[2],[3],[4]]))
# print(obj.countComponents(5, [[0,1],[1,2],[0,2],[3,4]]))