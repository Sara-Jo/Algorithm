k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lans:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)