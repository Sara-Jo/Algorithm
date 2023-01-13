from collections import deque

n = int(input())
graph = []
time = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark = [i, j, 2, 0]    # 상어의 위치(i, j), 크기, 먹은 물고기 수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    candidates = []
    q = deque([(x, y, 0)])

    while q:
        cur_x, cur_y, distance = q.popleft()

        for k in range(4):
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 빈 공간이거나 크기가 같은 물고기를 만난 경우
                if graph[nx][ny] == 0 or graph[nx][ny] == shark[2]:
                    q.append((nx, ny, distance + 1))
                    visited[nx][ny] = 1
                
                # 크기가 작은 물고기를 만난 경우
                elif graph[nx][ny] != 0 and graph[nx][ny] < shark[2]:
                    candidates.append((nx, ny, distance + 1))
                    visited[nx][ny] = 1

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(candidates, key=lambda x: (-x[2], -x[0], -x[1]))
 
time = 0          
while True:
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    c = bfs(shark[0], shark[1])

    if len(c) == 0:
        print(time)
        break

    x, y, dist = c.pop()
    time += dist
    shark[3] += 1

    # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    if shark[2] == shark[3]:
        shark[2] += 1
        shark[3] = 0

    graph[shark[0]][shark[1]] = 0
    graph[x][y] = 0
    shark[0], shark[1] = x, y
    graph[shark[0]][shark[1]] = 9
