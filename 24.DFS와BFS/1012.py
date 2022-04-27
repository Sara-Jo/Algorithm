import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)   

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)


# from collections import deque

# def bfs(a, b):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     queue = deque()
#     queue.append((a, b))
#     graph[a][b] = 0
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= nx < n) and (0 <= ny < m):
#                 if graph[nx][ny] == 1:
#                     queue.append((nx, ny))
#                     graph[nx][ny] = 0

# t = int(input())

# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0 for _ in range(m)] for _ in range(n)]
#     cnt = 0

#     for _ in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 cnt += 1
#                 bfs(i, j)

#     print(cnt)