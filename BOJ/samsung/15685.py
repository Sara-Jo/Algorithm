n = int(input())
graph = [[0] * 101 for _ in range(101)] # 드래곤 커브를 그릴 격자

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, input().split())  # y좌표, x좌표, 시작방향, 세대
    graph[x][y] = 1
    whole = [d] # 드래곤 커브가 연결된 선분
    now = [d]   # 현재 그리고 있는 드래곤커브의 세대(0 ~ g)

    for _ in range(g + 1):  # 0세대부터 g세대까지 그리기
        # 드래곤 커브 그리기
        for dir in now:
            x += dx[dir]
            y += dy[dir]
            graph[x][y] = 1

        now = [(i + 1) % 4 for i in whole]  # 이전 세대 방향 정보 가져오기
        now.reverse()   # 순서 뒤집기
        whole += now    # 드래곤 커브에 연결해주기

result = 0
 # 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수 파악
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            result += 1

print(result)