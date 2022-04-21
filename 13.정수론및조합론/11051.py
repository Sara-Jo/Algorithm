# 1 ---------------------------------------------
n, k = map(int, input().split())

d = [[0] * (i + 1) for i in range(n + 1)]
d[0][0] = 1

for i in range(1, n + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            d[i][j] = 1
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

print(d[n][k] % 10007)

# 2 ---------------------------------------------
# from math import factorial

# n, k = map(int, input().split())
# result = factorial(n) // factorial(n - k) // factorial(k)
# print(result % 10007)