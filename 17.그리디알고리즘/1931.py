n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0]))
count = 1
end = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end:
        count += 1
        end = meetings[i][1]
print(count)