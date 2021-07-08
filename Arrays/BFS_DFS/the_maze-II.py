from collections import deque
import heapq
class Solution:
    def shortestDistance(self, maze, start, destination):
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i , j in directions:
                d = 0
                nr = x+i
                nc = y+j
                while 0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc] != 1:
                    nr+=i
                    nc+=j
                    d+=1




obj = Solution()
print(obj.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
                     [0, 4], [4, 4]))
print(obj.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
                     [0, 4], [3, 2]))