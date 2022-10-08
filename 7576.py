from collections import deque

m, n = map(int, input().split())
tomatoes = []
q = deque([])

for i in range(n):
    tomatoes.append(list(map(int, input().split())))
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y =  q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    q.append((nx, ny))
                if tomatoes[nx][ny] > 1:
                    if tomatoes[nx][ny] > tomatoes[x][y] + 1:
                        tomatoes[nx][ny] = tomatoes[x][y] + 1
                        q.append((nx, ny))

bfs()

def get_result():
    result = 0
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0:
                return -1
            result = max(result, tomatoes[i][j])
    return result - 1

print(get_result())
