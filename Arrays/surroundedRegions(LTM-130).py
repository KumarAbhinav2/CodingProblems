class Solution:

    def solve(self, board):
        self.m = len(board)
        self.n = len(board[0])
        # lets iterate only over border cells and start dfs
        for r in range(self.m):
            for c in range(self.n):
                if r == 0 or r == self.m-1 or c == 0 or c== self.n-1:
                    self.dfs(board, r, c)
        for r in range(self.m):
            for c in range(self.n):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == 'E': board[r][c] = 'O'

    def dfs(self, board, row, col):
        if board[row][col] != 0:
            return
        board[row][col] = 'E'
        for r, c in [(-1,0), (0, -1), (1, 0), (0, 1)]:
            nr = r+row
            nc = c+col
            if 0<nr<self.m-1 and 0<nc<self.n-1:
                self.dfs(board, nr, nc)

    def bfs(self, board, rw, cl):
        from collections import deque
        queue = deque([(rw, cl)])
        while queue:
            row, col = queue.popleft()
            if board[row][col] != 'O':
                continue
            board[row][col] = 'E'
            for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr = r + row
                nc = c + col
                if 0 < nr < self.m - 1 and 0 < nc < self.n - 1:
                    queue.append((nr, nc))

    # Time Complexity: O(n) number of cells in board
    # Space Complecity: O(n), recursive dfs call stack