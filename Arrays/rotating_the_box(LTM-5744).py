
class Solution:
    def rotateTheBox(self, box):
        for r in range(len(box)):
            for c in range(len(box[0])-1, -1, -1):
                if box[r][c] == '.' and c > 0:
                    self.dfs(r, c, box)
        return list(zip(*box[::-1]))

    def dfs(self, x, y, box):
        if box[x][y - 1] != '*' and y > 0:
            box[x][y] = box[x][y - 1]
            box[x][y - 1] = '.'
            self.dfs(x, y-1, box)




obj = Solution()
#obj.rotateTheBox([['#', '.', '#']])
obj.rotateTheBox([['#', '.', '*', '.'],
                  ['#', '#', '*', '.']])

# obj.rotateTheBox([['#', '#', '*', '.', '*', '.'],
#                   ['#', '#', '#', '*', '.', '.'],
#                   ['#', '#', '#', '.', '#', '.']])