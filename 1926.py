from collections import deque

n, m = map(int, input().split())
painting = []
for _ in range(n):
    painting.append(list(map(int, input().split())))

painting_num = 0
max_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(q, index):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if painting[nx][ny] == 1:
                    q.append((nx, ny))
                    index += 1
                    painting[nx][ny] = 2
        if not q:
            return index

for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            painting_num += 1
            painting[i][j] = 2
            q = deque([(i, j)])
            max_area = max(max_area, bfs(q, 1))

print(painting_num)
print(max_area)