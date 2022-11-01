n = int(input())
k = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1 # 사과 위치

l = int(input())
moves = []
for _ in range(l):
    a, b = input().split()
    moves.append([int(a), b])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(c, direction):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def solve():
    x, y = 1, 1 # 뱀의 머리 좌표
    graph[x][y] = 2 # 뱀이 존재하는 위치 2로 표시
    snake = [(x, y)]    # 뱀이 차지하고 있는 좌표
    direction = 0   # 0: 동, 1: 남, 2: 서, 3: 북
    time = 0
    move_cnt = 0    # 방향 회전 횟수

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 < nx <= n and 0 < ny <= n and graph[nx][ny] != 2:  # 이동하는 좌표가 벽안쪽이고 뱀이 위치하는 곳이 아니면
            if graph[nx][ny] == 0:  # 빈칸으로 이동
                snake.append((nx, ny))  # 뱀 좌표 추가
                graph[nx][ny] = 2
                px, py = snake.pop(0)    # 꼬리 이동
                graph[px][py] = 0
                x, y = nx, ny   # 머리 이동
            elif graph[nx][ny] == 1:    # 사과로 이동
                snake.append((nx, ny))  # 뱀 좌표 추가(꼬리 이동 x)
                graph[nx][ny] = 2
                x, y = nx, ny   # 머리 이동
                
        else:
            time += 1
            return time

        time += 1
        if move_cnt < l and time == moves[move_cnt][0]:
            direction = turn(moves[move_cnt][1], direction)
            move_cnt += 1

print(solve())