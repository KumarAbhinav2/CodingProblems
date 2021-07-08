from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        directions = [(0, -1), (-1, -1), (0, 1), (1, 1),(-1, 1), (-1, 0), (1, 0), (1, -1)]
        if not grid:
            return 0
        q = deque()
        r = len(grid)
        c = len(grid[0])
        if grid[0][0] !=0 or grid[r-1][c-1] != 0:
            return -1
        q.append((0,0,1))
        visited = {(0,0)}
        while q:
            row, col, distance = q.popleft()
            if row == r-1 and col == c-1:
                return distance
            for i, j in directions:
                nr = row+i
                nc = col+j
                if 0<=nr<r and 0<=nc<c and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, distance+1))
        return -1

obj = Solution()
#ip = [[0, 0], [0, 0]]
ip = [[0,0,0],[1,1,0],[1,1,0]]
print(obj.shortestPathBinaryMatrix(ip))