n = int(input())
tree = [input() for _ in range(n)]

def compress(x, y, n):
    color = tree[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != tree[i][j]:
                print('(', end='')
                compress(x, y, n // 2)
                compress(x, y + n // 2, n // 2)
                compress(x + n // 2, y, n // 2)
                compress(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    print(color, end='')

compress(0, 0, n)