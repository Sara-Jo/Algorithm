t = int(input())

for _ in range(t):
    words = []
    n = int(input())
    for _ in range(n):
        words.append(input())
    words.sort()
    print(words)