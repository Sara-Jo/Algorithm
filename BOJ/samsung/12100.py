from copy import deepcopy

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

def move(board, dir):
    if dir == 0:    # 동쪽
        for i in range(n):  # i: 행(0 ~ n - 1)
            top = n - 1
            for j in range(n - 2, -1, -1):  # j: 열(n - 2 ~ 0)
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:  # top이 비어있을 때: top으로 숫자 이동
                        board[i][top] = tmp
                    elif board[i][top] == tmp:  # top과 같은 숫자일 때: top으로 숫자 합치기
                        board[i][top] = tmp * 2
                        top -= 1
                    else:   # top과 다른 숫자일 때
                        top -= 1
                        board[i][top] = tmp
    elif dir == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp
    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp
    else:  # 북쪽
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp
    return board

def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

answer = 0
dfs(data, 0)
print(answer)