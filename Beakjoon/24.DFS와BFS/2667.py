n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

cnt = 0
result = []

def dfs(i, j):
    global cnt
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if graph[i][j] == 1:
        cnt += 1
        graph[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for i in result:
    print(i)


# from collections import deque

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
# result = []

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(i, j):
#     queue = deque()
#     queue.append((i, j))
#     graph[i][j] = 0
#     cnt = 1
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 cnt += 1
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 0
#     return cnt

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             result.append(bfs(i, j))

# result.sort()
# print(len(result))
# for i in result:
#     print(i)