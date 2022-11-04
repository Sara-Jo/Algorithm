n, m, x, y, k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

moves = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

def move_dice(move):
    global dice
    a, b, c, d, e, f = dice
    if move == 1:
        dice = [d, b, a, f, e, c]
    elif move == 2:
        dice = [c, b, f, a, e, d]
    elif move == 3:
        dice = [e, a, c, d, f, b]
    else:
        dice = [b, f, c, d, a, e]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(len(moves)):
    nx = x + dx[moves[i] - 1]
    ny = y + dy[moves[i] - 1]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        move_dice(moves[i])
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])