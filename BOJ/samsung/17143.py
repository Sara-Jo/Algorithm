r, c, m = map(int, input().split())
sharks = [[0] * c for _ in range(r)]
for _ in range(m):
    x, y, speed, dir, size = map(int, input().split())
    sharks[x - 1][y - 1] = [speed, dir - 1, size]

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for time in range(c):
    # 상어 잡기
    for i in range(r):
        if sharks[i][time] != 0:
            answer += sharks[i][time][2]
            sharks[i][time] = 0
            break
    
    # 상어 이동
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if sharks[i][j] != 0:
                x, y, speed, dir, size = i, j, sharks[i][j][0], sharks[i][j][1], sharks[i][j][2]
                for _ in range(speed):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    # 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 이동
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        if dir == 0: dir = 1
                        elif dir == 1: dir = 0
                        elif dir == 2: dir = 3
                        elif dir == 3: dir = 2
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                    x, y = nx, ny

                if temp[x][y] == 0:
                    temp[x][y] = [speed, dir, size]
                else:   # 이동한 자리에 다른 상어가 있으면 큰 상어로 넣어주기
                    if temp[x][y][2] < size:
                        temp[x][y] = [speed, dir, size]
    sharks = temp

print(answer)