class Solution:
    def getBiggestThree(self, grid):
        self.r = len(grid[0])
        self.c = len(grid)
        self.d = [(1, 1), (-1,-1), (1,-1), (-1, 1)]
        for i in range(self.r):
            for j in range(self.c):
                if i not in [0, self.r-1] and j not in [0, self.c-1]:
                    self.dfs(i, j, [], grid)


    def dfs(self, i, j, area, grid):
        for r, c in self.d:
            nr = i+r
            nc = j+c
            if 0<=nr<self.r and 0<=nc<self.c:
                area.append(grid[nr, nc])
                self.dfs(nr, nc, area, grid)

