class Solution:
    def findPaths_bf(self, m, n, maxMove, startRow, startColumn):
        if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
            return 1
        if maxMove == 0:
            return 0
        return self.findPaths_bf(m, n, maxMove-1, startRow-1, startColumn)+\
            self.findPaths_bf(m, n, maxMove-1, startRow+1, startColumn)+\
            self.findPaths_bf(m, n, maxMove-1, startRow, startColumn-1)+\
            self.findPaths_bf(m, n, maxMove-1, startRow, startColumn+1)

    # Time: O(4**n)
    # Space: O(N)

    def findPaths_bf_memo(self, m, n, maxMove, startRow, startColumn):
        memo = [[[[-1]*(maxMove+1) for _ in range(n+1)]] for _ in range(m+1)]
        def rec(startRow, startColumn , maxMove):
            if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
                return 1
            if maxMove == 0:
                return 0

            if memo[startRow][startColumn][maxMove]!=-1:
                pass
        return self.findPaths_bf(m, n, maxMove-1, startRow-1, startColumn)+\
            self.findPaths_bf(m, n, maxMove-1, startRow+1, startColumn)+\
            self.findPaths_bf(m, n, maxMove-1, startRow, startColumn-1)+\
            self.findPaths_bf(m, n, maxMove-1, startRow, startColumn+1)

    def _find_paths(self, m, n, maxMove, startRow, startColumn, memo):
        pass

obj = Solution()
print(obj.findPaths_bf(2, 2, maxMove=2, startRow=0, startColumn=0))

