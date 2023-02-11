t = int(input())

for _ in range(t):
    n, l, f = map(int, input().split())
    words = list(map(str, input().split()))
    for i in range(n):
        words[i] = words[i][::-1]
    words.sort()

    count = 0
    i = 0
    while i < n - 1:
        if words[i][:f] == words[i + 1][:f]:
            count += 1
            i += 1
        i += 1
    print(count)