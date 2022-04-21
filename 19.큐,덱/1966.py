from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = deque(list(map(int, input().split())))
    cnt = 0
    while True:
        if priority[0] == max(priority):
            cnt += 1
            if m == 0:
                print(cnt)
                break
            else:
                priority.popleft()
                m -= 1
        else:
            priority.append(priority[0])
            priority.popleft()
            m -= 1
            if m < 0:
                m = len(priority) - 1