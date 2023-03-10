def solution(m, n, board):
    for i in range(m):
        x = list(board[i])
        board[i] = x
    
    while True:
        to_remove = []

        # 4개 붙어있는 블록 찾아서 블록의 첫째 칸을 to_remove에 저장
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] == 0:
                    continue
                if board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y] and board[x][y] == board[x+1][y+1]:
                    to_remove.append((x, y))

        # 지울 블록 없으면 반복문 탈출
        if len(to_remove) == 0:
            break
        
        # 블록 지우기 (0으로 값 변경)
        for x, y in to_remove:
            board[x][y] = 0
            board[x][y+1] = 0
            board[x+1][y] = 0
            board[x+1][y+1] = 0

        # 블록 아래로 떨어져 빈공간 채우기
        while True:
            moved = 0
            for x in range(m-1):
                for y in range(n):
                    if board[x][y] != 0 and board[x+1][y] == 0:
                        board[x+1][y] = board[x][y]
                        board[x][y] = 0
                        moved = 1
            if moved == 0:
                break
                
    answer = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
                
    return answer