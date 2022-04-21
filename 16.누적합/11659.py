import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]

tmp = 0
for i in nums:
    tmp += i
    prefix_sum.append(tmp)


for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])