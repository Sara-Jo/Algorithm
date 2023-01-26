n, k = map(int, input().split())
board = [[0] * (n + 1)] # 체스판의 정보가 담긴 리스트
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

pieces = [] # 말의 위치 정보가 담긴 리스트(x, y, dir)
chess = [[[] for _ in range(n + 1)] for _ in range(n + 1)]    # 말의 위치 정보가 담긴 2차원 리스트(말의 인덱스)
for i in range(k):
    x, y, dir = map(int, input().split())
    chess[x][y].append(i)
    pieces.append([x, y, dir])


# 방향 반대로 바꾸기
def change_dir(dir):
    if dir in [1, 3]:
        dir += 1
    elif dir in [2, 4]:
        dir -= 1
    return dir


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

is_done = False
for time in range(1, 1000):
    for i, piece in enumerate(pieces):
        x, y, dir = piece
        nx = x + dx[dir - 1]
        ny = y + dy[dir - 1]

        # 파란 칸으로 이동 혹은 체스판을 벗어나는 경우: 방향 반대로 바꾸고 한 칸 이동
        if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 2:
            dir = change_dir(dir)
            pieces[i][2] = dir
            nx = x + dx[dir - 1]
            ny = y + dy[dir - 1]
            # 방향을 바꿔서 이동하려는 곳이 체스판을 벗어나거나 파란 칸인 경우 움직이지 않고 넘어감
            if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 2:
                continue

        # 흰색 칸 혹은 빨간 칸으로 이동
        if board[nx][ny] == 0 or board[nx][ny] == 1:
            moving_pieces = []  # 이동해야할 말
            for j, chess_num in enumerate(chess[x][y]):
                if chess_num == i:
                    moving_pieces = chess[x][y][j:]
                    if board[nx][ny] == 0:
                        chess[nx][ny].extend(moving_pieces)
                    else:   # 빨간 칸이면 거꾸로 뒤집어서 이동
                        chess[nx][ny].extend(moving_pieces[::-1])
                    chess[x][y] = chess[x][y][:j]
                    break
            for moving_piece in moving_pieces:
                pieces[moving_piece][0] = nx
                pieces[moving_piece][1] = ny
    
        if len(chess[nx][ny]) >= 4:
            print(time)
            is_done = True
            break
    
    if is_done:
        break
else:
    print(-1)