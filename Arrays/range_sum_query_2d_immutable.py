class NumMatrix:

    def __init__(self, matrix):
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                res+=self.mat[row][col]
        return res


class NumMatrix2:

    def __init__(self, matrix):
        self.mat = matrix
        self.numArray(matrix)

    def numArray(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        self.dp = [[0] * (len(matrix[0]) + 1)] * len(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            res += self.dp[row][col2 + 1] - self.dp[row][col1]
        return res

    # Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix2([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
# print(obj.sumRegion(1, 1, 2, 2))
# print(obj.sumRegion(1, 2, 2, 4))