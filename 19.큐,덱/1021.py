from collections import deque

n, m = map(int, input().split())
d = deque([i for i in range(1, n + 1)])
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    if d.index(i) < len(d) / 2:
        while d[0] != i:
            d.append(d[0])
            d.popleft()
            cnt += 1
    else:
        while d[0] != i:
            d.appendleft(d[-1])
            d.pop()
            cnt += 1
    d.popleft()

print(cnt)