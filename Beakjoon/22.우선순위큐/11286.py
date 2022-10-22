import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap):
            n = heapq.heappop(heap)
            print(n[0] * n[1])
        else:
            print(0)
    else:
        abs = a if a > 0 else -a
        sign = 1 if a > 0 else -1
        heapq.heappush(heap, [abs, sign])