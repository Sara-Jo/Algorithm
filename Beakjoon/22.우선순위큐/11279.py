import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a:
        heapq.heappush(heap, (-a))
    else:
        if len(heap):
            print(-1 * heapq.heappop(heap))
        else:
            print(0)