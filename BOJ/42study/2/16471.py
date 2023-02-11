n = int(input())
juon = list(map(int, input().split()))
owner = list(map(int, input().split()))

juon.sort()
owner.sort()

i = 0
wins = 0
for card in juon:
    while i < n:
        if card < owner[i]:
            wins += 1
            i += 1
            break
        i += 1

result = "YES" if wins >= (n + 1) / 2 else "NO"
print(result)