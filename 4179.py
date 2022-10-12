from collections import deque

r, c = map(int, input().split())
maze = []

for i in range(r):
    maze.append(list(input()))
    for j in range(c):
        if maze[i][j] == 'J':
            # 지훈이 이동 좌표 (시간, x좌표, y좌표)
            q = deque([(0, i, j)])

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            # 불 이동 좌표 (시간은 필요없으므로 -1, x좌표, y좌표)
            q.append((-1, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()

    # 지훈이가 탈출 가능하면
    if time > -1 and maze[x][y] != 'F' and (x == 0 or y == 0 or x == r - 1 or y == c - 1):
        result = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지훈이 이동
        if time > -1 and 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.':
            # 지훈이가 이미 방문한 곳은 '_'로 표시
            maze[nx][ny] = '_'
            q.append((time + 1, nx, ny))

        # 불 퍼뜨리기
        if time == -1 and 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#' and maze[nx][ny] != 'F':
            maze[nx][ny] = 'F'
            q.append((-1, nx, ny))

print(result)