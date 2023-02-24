class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 -> 1: 2
        # 1 -> 0: 3

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        n = len(board)
        m = len(board[0])
        for x in range(n):
            for y in range(m):
                count = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and (board[nx][ny] == 1 or board[nx][ny] == 3):
                        count += 1
                if board[x][y] == 1:
                    if count < 2 or count > 3:
                        board[x][y] = 3
                else:
                    if count == 3:
                        board[x][y] = 2

        for x in range(n):
            for y in range(m):
                if board[x][y] == 2:
                    board[x][y] = 1
                elif board[x][y] == 3:
                    board[x][y] = 0
