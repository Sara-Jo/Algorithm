import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

tmp = 0
for i in range(n):
    tmp += table[0][i]
    prefix_sum[1][i + 1] = tmp

for i in range(2, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        tmp += table[i - 1][j - 1]
        prefix_sum[i][j] = prefix_sum[i - 1][j] + tmp

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    print(result)