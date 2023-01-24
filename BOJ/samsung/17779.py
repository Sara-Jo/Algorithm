def separate(x, y, d1, d2):
    # 5번 선거구 경계선 표시
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5
    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        temp[x + d2 + i][y + d2 - i] = 5

    population = [0] * 5
    # 1번 선거구
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if temp[i][j] == 5:
                break
            else:
                population[0] += graph[i][j]

    # 2번 선거구
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if temp[i][j] == 5:
                break
            else:
                population[1] += graph[i][j]

    # 3번 선거구
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if temp[i][j] == 5:
                break
            else:
                population[2] += graph[i][j]

    # 4번 선거구
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y + d2 - d1 - 1, -1):
            if temp[i][j] == 5:
                break
            else:
                population[3] += graph[i][j]

    population[4] = total_sum - sum(population)
    return max(population) - min(population)


def makeBorder(x, y):
    min_gap = 1e9
    for d1 in range(1, n + 1):
        for d2 in range(1, n + 1):
            if x + d1 + d2 > n:
                continue
            if y - d1 < 1:
                continue
            if y + d2 > n:
                continue
            min_gap = min(min_gap, separate(x, y, d1, d2))
    return min_gap


n = int(input())
graph = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

total_sum = 0
for i in range(1, n + 1):
    total_sum += sum(graph[i])

answer = 1e9
for x in range(1, n + 1):
    for y in range(1, n + 1):
        answer = min(answer, makeBorder(x, y))

print(answer)