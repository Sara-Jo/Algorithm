from itertools import combinations
from collections import deque
import copy

def bfs(virus):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    result = 0

    visited = [[-1] * n for _ in range(n)]
    for x, y in virus:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if lab[nx][ny] == 2:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                if lab[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny])
    
    virus_count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                virus_count += 1

    return result if virus_count == open_space_count else 1e9


n, m = map(int, input().split())
lab = []
virus = []
open_space_count = 0

for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 2:  # 바이러스가 있는 곳
            virus.append((i, j))
        if lab[i][j] != 1:  # 벽이 아닌 곳(바이러스가 모두 퍼져야 하는 곳)
            open_space_count += 1

answer = 1e9
for candidate in combinations(virus, m):
    answer = min(answer, bfs(candidate))

print(answer if answer != 1e9 else -1)