from collections import deque
class Solution:
    def isBipartite(self, graph) -> bool:
        q = deque()
        colored = {}
        for i in range(len(graph)):
            if i not in colored and graph[i]:
                q.append(i)
                colored[i] = True
                while q:
                    node = q.popleft()
                    for neighbour in graph[node]:
                        if neighbour not in colored:
                            colored[neighbour] = not colored[node]
                            q.append(neighbour)
                        elif colored[neighbour] == colored[node]:
                            return False
        return True

obj = Solution()
print(obj.isBipartite([[],[3],[],[1],[]]))