from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = [[0] * m for _ in range(n)]

empty_area = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_area.append((i, j))

def spread_virus(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            spread_virus(nx, ny)

def get_safe_area():
    ret = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                ret += 1
    return ret

candidates = list(combinations(empty_area, 3))

result = 0
for candidate in candidates:
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    for spot in candidate:
        (a, b) = spot
        temp[a][b] = 1
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                spread_virus(i, j)
    safe = get_safe_area()
    result = max(result, safe)

print(result)

#--------------------------------------------------------------------

n, m = map(int, input().split())
data = []   # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
