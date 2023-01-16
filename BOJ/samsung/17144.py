r, c, t = map(int, input().split())
graph = []
purifier = []
for i in range(r):
    graph.append(list(map(int, input().split())))
    for j in range(c):
        if graph[i][j] == -1:
            purifier.append((i, j))


def spread(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    candidates = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] >= 0:
            candidates.append((nx, ny))

    return candidates


def purify_up():
    # 동, 북, 서, 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    before = 0  # 이전 값
    x, y = purifier[0][0], 1    # 시작 지점
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == purifier[0][0] and y == 0:  # 처음 위치로 되돌아오면 종료
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:  # 맵을 벗어나는 곳이면 방향바꾸고 건너뛰기
            direction += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny


def purify_down():
    # 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    before = 0
    x, y = purifier[1][0], 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == purifier[1][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny


for _ in range(t):
    temp = [[0] * c for _ in range(r)]

    # 확산
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                candidates = spread(i, j)
                for x, y in candidates:
                    temp[x][y] += graph[i][j] // 5
                graph[i][j] -= graph[i][j] // 5 * len(candidates)

    for i in range(r):
        for j in range(c):
            if temp[i][j] > 0:
                graph[i][j] += temp[i][j]

    # 공기 청정
    purify_up()
    purify_down()


answer = 0
for i in range(r):
    answer += sum(graph[i])

print(answer + 2)