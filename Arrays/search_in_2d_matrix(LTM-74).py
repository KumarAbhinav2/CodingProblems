class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        r = 0
        c = len(matrix[0])-1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target:
                r+=1
            elif matrix[r][c] > target:
                c-=1
            else:
                return True
        return False

    # Time: O(log(mn))
    # Space: O(1)

obj = Solution()
# obj.searchMatrix([[1,4,7,11,15],
#                   [2,5,8,12,19],
#                   [3,6,9,16,22],
#                   [10,13,14,17,24],
#                   [18,21,23,26,30]], 5)
#obj.searchMatrix([[1, 1]], 2)
obj.searchMatrix([[1]], 1)
#obj.searchMatrix([[5], [6]], 6)