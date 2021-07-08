class Solution:
    def rotateGrid(self, grid, k: int):
        l = 0
        r = len(grid[0])-1
        t = 0
        b = len(grid)-1
        while l < r and t < b:
            for j in range(k):
                prev = grid[t + 1][r]
                for i in range(r, -1, -1):
                    curr = grid[t][i]
                    grid[t][i] = prev
                    prev = curr
                t +=1

                for i in range(t, b+1):
                    curr = grid[i][l]
                    grid[i][l] = prev
                    prev = curr
                l+=1

                for i in range(l, r+1):
                    curr = grid[b][i]
                    grid[b][i] = prev
                    prev = curr
                b-=1

                for i in range(b, -1, -1):
                    curr = grid[i][r]
                    grid[i][r] = prev
                    prev = curr

                r-=1

        return grid


obj = Solution()
#print(obj.rotateGrid([[40,10],[30,20]], 1))
print(obj.rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2))

