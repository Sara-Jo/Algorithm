n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
max_val = max(map(max, graph))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * m for _ in range(n)]

def dfs(x, y, cnt, val):
    global result
    if val + max_val * (4 - cnt) <= result:
        return
    if cnt == 4:
        result = max(result, val)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, val + graph[nx][ny])
            visited[nx][ny] = 0

def exception(x, y):
    global result
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])
    if len(arr) >= 3:
        arr.sort(reverse=True)
        result = max(result, graph[x][y] + arr[0] + arr[1] + arr[2])

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
        exception(i, j)

print(result)