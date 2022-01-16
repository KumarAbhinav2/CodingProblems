class Solution:
    def wallsAndGates(self, rooms) -> None:
        if not rooms: return
        from collections import deque
        q = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        gate = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        empty = 2147483647
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == gate:
                    q.append((r, c))

        while q:
            i, j = q.popleft()
            for r, c in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and rooms[nr][nc] == empty:
                    rooms[nr][nc] = rooms

        # Time: O(mn)
        # Space: O(mn)