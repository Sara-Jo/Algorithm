n = int(input())
wine = [0] * 10001
for i in range(n):
    wine[i] = int(input())
d = [0] * 10001
d[0] = wine[0]
d[1] = wine[0] + wine[1]
d[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2])

for i in range(3, n):
    d[i] = max(wine[i] + wine[i - 1] + d[i - 3], wine[i] + d[i - 2], d[i - 1])

print(d[n - 1])
