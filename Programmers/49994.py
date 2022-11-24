def solution(dirs):
    visit = set()
    x, y = 5, 5

    for dir in dirs:
        if dir == 'U' and x < 10:
            visit.add(((x, y), (x + 1, y)))
            x += 1
        elif dir == 'D' and x > 0:
            visit.add(((x - 1, y), (x, y)))
            x -= 1
        elif dir == 'R' and y < 10:
            visit.add(((x, y), (x, y + 1)))
            y += 1
        elif dir == 'L' and y > 0:
            visit.add(((x, y - 1), (x, y)))
            y -= 1

    return len(visit)