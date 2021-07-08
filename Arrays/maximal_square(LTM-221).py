class Solution:

    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1: return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r][c], dp[r+1][c])+1
                    max_side = max(max_side, dp[r+1][c+1])
        return max_side*max_side