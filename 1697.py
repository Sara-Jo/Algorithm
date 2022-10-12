from collections import deque

n, k = map(int, input().split())
map = [0] * 100001
map[n] = 1

q = deque([(0, n)])

result = 0

def get_nx(num, type):
    if type == 0:
        return num - 1
    if type == 1:
        return num + 1
    if type == 2:
        return num * 2

while q:
    time, x = q.popleft()

    if x == k:
        result = time
        break

    for i in range(3):
        nx = get_nx(x, i)
        if 0 <= nx <= 100000 and map[nx] == 0:
            map[nx] = 1
            q.append((time + 1, nx))

print(result)
