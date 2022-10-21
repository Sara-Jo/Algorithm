n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            data[i][j] = data[i][j] + data[i - 1][j]
        elif j == i:
            data[i][j] = data[i][j] + data[i - 1][j - 1]
        else:
            data[i][j] = data[i][j] + max(data[i - 1][j], data[i - 1][j - 1])

result = 0
for i in range(n):
    result = max(result, data[n - 1][i])

print(result)