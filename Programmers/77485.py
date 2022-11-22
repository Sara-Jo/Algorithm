def rotate(graph, query):
    x1, y1, x2, y2 = query
    min_val = graph[x1][y1]
    start = graph[x1][y1]

    # 아래로 이동
    for i in range(x2 - x1):
        graph[x1 + i][y1] = graph[x1 + i + 1][y1]
        min_val = min(min_val, graph[x1 + i + 1][y1])

    # 오른쪽으로 이동
    for i in range(y2 - y1):
        graph[x2][y1 + i] = graph[x2][y1 + i + 1]
        min_val = min(min_val, graph[x2][y1 + i + 1])

    # 위로 이동
    for i in range(x2 - x1):
        graph[x2 - i][y2] = graph[x2 - i - 1][y2]
        min_val = min(min_val, graph[x2 - i - 1][y2])

    # 왼쪽으로 이동
    for i in range(y2 - y1):
        graph[x1][y2 - i] = graph[x1][y2 - i - 1]
        min_val = min(min_val, graph[x1][y2 - i])

    graph[x1][y1 + 1] =  start

    return graph, min_val

def solution(rows, columns, queries):
    answer = []

    # 행렬 만들기
    graph = [[0] * (columns + 1) for _ in range(rows + 1)]
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            graph[i][j] = num
            num += 1

    # 회전
    for query in queries:
        graph, min_val = rotate(graph, query)
        answer.append(min_val)

    return answer