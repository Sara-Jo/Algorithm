from collections import deque

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R': 
            red_x, red_y = i, j
        elif board[i][j] == 'B':
            blue_x, blue_y = i, j 

q = deque([])
q.append((red_x, red_y, blue_x, blue_y, 1))
visited = []
visited.append((red_x, red_y, blue_x, blue_y))

def move(x, y, dx, dy):
    cnt = 0 # 이동 칸 수
    # 다음 칸이 벽이거나 구멍에 도달할 때 까지
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve():
    while q:
        red_x, red_y, blue_x, blue_y, depth = q.popleft()
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            red_nx, red_ny, red_cnt = move(red_x, red_y, dx[i], dy[i])  # red 이동
            blue_nx, blue_ny, blue_cnt = move(blue_x, blue_y, dx[i], dy[i]) # blue 이동
            if board[blue_nx][blue_ny] != 'O':  # 실패 조건이 아니면(파란 구슬이 구멍에 들어가지 않았으면)
                if board[red_nx][red_ny] == 'O':    # 성공 조건(빨간 구슬이 구멍에 들어갔으면)
                    print(depth)
                    return 
                if red_nx == blue_nx and red_ny == blue_ny: # 빨간 구슬과 파란 구슬이 겹쳤을 때
                    if red_cnt > blue_cnt:  # 이동 거리가 더 많은 구슬을
                        red_nx -= dx[i] # 한 칸 뒤로
                        red_ny -= dy[i]
                    else:
                        blue_nx -= dx[i]
                        blue_ny -= dy[i]
                if (red_nx, red_ny, blue_nx, blue_ny) not in visited:
                    visited.append((red_nx, red_ny, blue_nx, blue_ny))
                    q.append((red_nx, red_ny, blue_nx, blue_ny, depth + 1))
    print(-1)   # 실패 시

solve()