class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = r + dx
            ny = c + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                self.dfs(grid, nx, ny)

from collections import deque
class Solution_BFS:
    def numIslands(self, grid) -> int:
        islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    q = deque([(i, j)])
                    grid[i][j] = '0'
                    while q:
                        r, c = q.popleft()
                        for x, y in directions:
                            nr = x + r
                            nc = y + c
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr, nc))
                    islands += 1

        return islands

obj = Solution_BFS()
obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])





