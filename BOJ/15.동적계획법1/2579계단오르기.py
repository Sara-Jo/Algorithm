n = int(input())
stair = [0] * 300
d = [0] * 300
for i in range(n):
    stair[i] = int(input())

d[0] = stair[0]
d[1] = stair[0] + stair[1]
d[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    d[i] = max(d[i - 3] + stair[i - 1] + stair[i], d[i - 2] + stair[i])

print(d[n - 1])