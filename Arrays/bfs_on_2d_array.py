
class Solution:
    def bfs(self, grid):
        q = []
        r = len(grid)
        c = len(grid[0])
        visited = [[0 for _ in range(c)] for j in range(r)]
        q.append((0, 0))
        while len(q)!=0:
            row, col = q.pop(0)
            if 0<=row<r and 0<=col<c and visited[row][col] == 0:
                visited[row][col] = True
                print(grid[row][col])
                q.append((row, col - 1))
                q.append((row, col + 1))
                q.append((row-1, col))
                q.append((row+1, col))

class Solution2:
    def bfs_8x(self, grid):
        q = []
        r = len(grid)
        c = len(grid[0])
        visited = [[0 for _ in range(c)] for j in range(r)]
        q.append((0, 0))
        while len(q)!=0:
            row, col = q.pop(0)
            if 0<=row<r and 0<=col<c and visited[row][col] == 0:
                visited[row][col] = True
                print(grid[row][col])
                q.append((row, col - 1))
                q.append((row-1, col - 1))
                q.append((row+1, col + 1))
                q.append((row, col + 1))
                q.append((row-1, col + 1))
                q.append((row-1, col))
                q.append((row+1, col))
                q.append((row+1, col - 1))




obj = Solution2()
ip=  [[1, 2, 3, 5],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
obj.bfs_8x(ip)