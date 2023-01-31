x = int(input())
line = list(map(str, input()))

line_len = len(line)
gap = 0
for i in range(line_len):
    if line[i] == 'M':
        gap += 1
        if gap > x and i < line_len - 1 and line[i + 1] == 'W':
            line[i], line[i + 1] = line[i + 1], line[i]
            gap -= 2
    else:
        gap -= 1
        if gap < -x and i < line_len - 1 and line[i + 1] == 'M':
            line[i], line[i + 1] = line[i + 1], line[i]
            gap += 2

    if abs(gap) > x:
        print(i)
        break

else:
    print(line_len)

    