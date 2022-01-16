from collections import deque
class Solution:

    def canReach_bfs(self, arr, start):
        q = deque([start])

        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue

            for d in [node + arr[node], node - arr[node]]:
                if 0<=d<len(arr):
                    q.append(d)

            arr[node] = -arr[node]
        return False

    # Time: O(N)
    # Space: O(N)

    def canReach_dfs(self, arr, start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]

            return self.canReach_dfs(arr, start + arr[start]) or self.canReach_dfs(arr, start - arr[start])
        return False

    # Time: O(N)
    # Space: O(N)