from collections import deque

n, m = map(int, input().split())
cows = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    cows[a].append(b)
    cows[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1

def dfs(arr):
    for cow in arr:
        if visited[cow] == 0:
            visited[cow] = 1
            dfs(cows[cow])

dfs(cows[1])

# q = deque([1])
# visited = [0] * (n + 1)
# visited[1] = 1

# while q:
#     current = q.popleft()
#     for cow in cows[current]:
#         if visited[cow] == 0:
#             q.append(cow)
#             visited[cow] = 1

for i in range(2, n + 1):
    if visited[i] == 0:
        print(i)