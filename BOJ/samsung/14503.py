n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0 
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

def turn_left(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

def solve(x, y, d):
    global result

    while True:
        # 1. 현재 위치를 청소한다.
        if graph[x][y] == 0:
            graph[x][y] = 2
            result += 1 # 청소한 칸의 개수
        cnt = 0 # 방향 회전 횟수
        while True:
            # 왼쪽방향 위치 체크
            nx = x + dx[turn_left(d)]
            ny = y + dy[turn_left(d)]
            # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
            if graph[nx][ny] == 0:
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
                d = turn_left(d)
                x, y = nx, ny
                break
            # 2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            elif graph[nx][ny] != 0 and cnt != 4:
                d = turn_left(d)
                cnt += 1
                continue
            # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
            elif graph[nx][ny] != 0 and cnt == 4:
                nx = x + dx[(d + 2) % 4]
                ny = y + dy[(d + 2) % 4]
                # 2-4. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                if graph[nx][ny] == 1:
                    return
                # 2-3. 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
                else:
                    x, y = nx, ny
                    break

solve(x, y, d)
print(result)