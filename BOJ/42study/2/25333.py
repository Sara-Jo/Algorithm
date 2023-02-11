t = int(input())

answer = []

for _ in range(t):
    a, b, x = map(int, input().split())
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        divisor = small
    else:
        divisor = min(big - small * (big // small), abs(big - small * (big // small + 1)))
    print(x // divisor)