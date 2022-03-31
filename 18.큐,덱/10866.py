from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
for _ in range(n):
    a = list(input().split())
    if a[0] == 'push_front':
        d.appendleft(a[1])
    elif a[0] == 'push_back':
        d.append(a[1])
    elif a[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif a[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif a[0] == 'size':
        print(len(d))
    elif a[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif a[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])