from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def bfs(x, y):
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == "1":
                        q.append((nx, ny))
                        grid[nx][ny] = 2

        answer = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    bfs(x, y)
                    answer += 1

        return answer