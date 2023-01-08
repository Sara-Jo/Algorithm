class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j, c in enumerate(board[i]):
                if c == word[0]:
                    if self.bfs(i, j, board, word) == True:
                        return True
        return False

    def bfs(self, x, y, board, word):

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n = len(board)
        m = len(board[0])

        q = deque([(x, y, 0, [(x, y)])])

        while q:
            x, y, count, visited = q.popleft()
            if count == len(word) - 1:
                return True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == word[count + 1] and (nx, ny) not in visited:
                    tmp = visited.copy()
                    tmp.append((nx, ny))
                    q.append((nx, ny, count + 1, tmp))
            
        return False