n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def is_possible_way(x):
    installed = [False for _ in range(n)]
    for i in range(n - 1):

        # 둘의 높이가 같은 경우
        if x[i] == x[i + 1]:
            continue

        # 높이 차이가 1이 아닌 경우
        if abs(x[i] - x[i + 1]) > 1:
            return False

        # 왼쪽 높이가 더 높은 경우: 오른쪽에 설치 가능한지 탐색 
        elif x[i] > x[i + 1]:
            temp_h = x[i + 1]
            for j in range(i + 1, i + 1 + l):
                # 지도 범위 밖을 벗어나면 False
                if j < 0 or j >= n:
                    return False
                # 낮은 곳의 높이가 다르거나 이미 설치된 곳이면 False
                if x[j] != temp_h or installed[j] == True:
                    return False
                installed[j] = True

        # 오른쪽 높이가 더 높은 경우: 왼쪽에 설치 가능한지 탐색
        elif x[i] < x[i + 1]:
            temp_h = x[i]
            for j in range(i, i - l, -1):
                if j < 0 or j >= n:
                    return False
                if x[j] != temp_h or installed[j] == True:
                    return False
                installed[j] = True

    return True
            
result = 0
# 행 체크
for i in range(n):
    if is_possible_way(graph[i]):
        result += 1

# 열 체크
for j in range(n):
    temp = []
    for i in range(n):
        temp.append(graph[i][j])
    if is_possible_way(temp):
        result += 1

print(result)