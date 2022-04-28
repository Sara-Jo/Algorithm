n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)


# from collections import deque

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# cnt = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def bfs(v):
#     global cnt
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         x = queue.popleft()
#         for i in graph[x]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 cnt += 1

# bfs(1)
# print(cnt)