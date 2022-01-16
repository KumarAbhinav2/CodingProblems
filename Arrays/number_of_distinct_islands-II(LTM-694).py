class Solution:
    def numDistinctIslands(self, grid) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        shapes = set()
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    shapes.add(self.dfs(i, j, grid, (i, j), [(i, j)]))
        return len(shapes)

    def dfs(self, x, y, grid, pos, directions):
        grid[x][y] = 0
        for m, n in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = m + x
            nc = n + y
            if 0 <= nr < self.r and 0 <= nc < self.c and grid[nr][nc] == 1:
                t_dir = (pos[0] + nr, pos[1] + nc)
                directions.append(t_dir)
                self.dfs(nr, nc, grid, t_dir, directions)
        return tuple(directions)


obj = Solution()
ip = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
print(obj.numDistinctIslands(ip))