n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus_one = 0
zero = 0
one = 0

def cut(x, y, n):
    global minus_one, zero, one
    num = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        cut(x + n // 3 * k, y + n // 3 * l, n // 3)
                return
    if num == -1:
        minus_one += 1
    elif num == 0:
        zero += 1
    else:
        one += 1

cut(0, 0, n)
print(minus_one)
print(zero)
print(one)