class Solution:
    def largestMagicSquare(self, grid):
        self.r = grid
        self.c = grid[0]
        l = min(self.r, self.c)
        for k in range(l, 1, -1):
            for i in range(self.r-k+1):
                for j in range(self.c-k+1):
                    if self.isMagicSquare(i, j, k):
                        return k
