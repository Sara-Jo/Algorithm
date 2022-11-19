import copy

n, m = map(int, input().split())
graph = []
cctv_list = []

# 0: 북, 1: 동, 2: 남, 3: 서
direction = [
    [], 
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] in [1, 2, 3, 4, 5]:
            cctv_list.append([graph[i][j], i, j])   # [cctv 번호, x 좌표, y 좌표] 저장 


# 해당 CCTV의 종류에서 바라보는 방향에 따라 감시할 수 있는 곳은 7로 변환, 벽을 만나거나 범위를 넘어가면 종료
def watch(graph, direction, x, y):
    for i in direction:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 7


def dfs(depth, arr):
    global min_value

    # cctv 개수만큼 감시를 다 했을 때 사각지대의 최소값 갱신
    if depth == len(cctv_list):
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(0)
        min_value = min(min_value, cnt)
        return

    tmp = copy.deepcopy(arr)
    cctv, x, y = cctv_list[depth]
    for i in direction[cctv]:
        # CCTV 감시영역 구하는 함수 호출
        watch(tmp, i, x, y)
        # 현재 Case에서 타 모든 CCTV 재귀적 탐색
        dfs(depth + 1, tmp)
        # CCTV를 다른 방향으로 회전시킨 후 재탐색하기 위함
        tmp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)