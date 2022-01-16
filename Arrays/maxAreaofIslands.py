class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        max_area = 0
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, grid, 1)
                    max_area = max(area, max_area)
        return max_area

    def dfs(self, r, c, grid, area):
        grid[r][c] = 0
        for i, j in self.directions:
            nr = i + r
            nc = j + c
            if 0 <= nr < self.r and 0 <= nc < self.c and grid[nr][nc] == 1:
                area += 1
                self.dfs(nr, nc, grid, area)
        return area

obj = Solution()
obj.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])