from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n + 1)])
print('<', end='')
while arr:
    for _ in range(k - 1):
        tmp = arr.popleft()
        arr.append(tmp)
    print(arr.popleft(), end='')
    if arr:
        print(', ', end='')
print('>', end='')