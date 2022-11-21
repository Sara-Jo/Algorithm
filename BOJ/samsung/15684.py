n, m, h = map(int, input().split())
visited = [[False] * (n + 1) for _ in range(h + 1)] # 사다리가 이미 있는 곳 방문 처리
combi = []  # 사다리를 놓을 수 있는 후보군
for _ in range(m):  
    a, b = map(int, input().split())
    visited[a][b] = True

# 모든 사다리가 동일한 위치에 도착하는지 확인
def check():
    for i in range(1, n + 1):
        now = i # 현재 위치(세로선)

        for j in range(1, h + 1):
            # 왼쪽으로 가로선이 있으면 왼쪽으로 이동
            if visited[j][now - 1]:
                now -= 1
            # 오른쪽으로 가로선이 있으면 오른쪽으로 이동
            elif visited[j][now]:
                now += 1

        if now != i:
            return False
    return True

def dfs(depth, idx):
    global answer

    if depth >= answer:
        return

    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        # 사다리를 놓을 수 있는지 다시 확인하고, 사다리를 놓은 후 dfs 함수로 재귀
        if not visited[x][y - 1] and not visited[x][y + 1]:
            visited[x][y] = True
            dfs(depth + 1, c + 1)
            visited[x][y] = False

for i in range(1, h + 1):
    for j in range(1, n):
        # 가로선이 접하면 안되므로 왼쪽, 해당 위치, 오른쪽에 전부 가로선이 없는지 확인
        if not visited[i][j - 1] and not visited[i][j] and not visited[i][j + 1]:
            combi.append([i, j])    

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)