class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if self.dfs(i, j, board, word[1:]):
                        return True
                    board[i][j] = word[0]
        return False

    def dfs(self, x, y, board, word):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        if len(word) == 0:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == word[0]:
                board[nx][ny] = '#'
                if self.dfs(nx, ny, board, word[1:]):
                    return True
                board[nx][ny] = word[0]
        return False