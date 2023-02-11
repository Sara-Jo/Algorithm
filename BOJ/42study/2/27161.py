def changeDirection(dir):
    if dir == -1:
        return 1
    else:
        return -1

n = int(input())
shout = 1
direction = 1

for _ in range(n):
    clock, time = map(str, input().split())
    
    # 과부하의 법칙 or 법칙 적용 X
    if (clock == "HOURGLASS" and shout == int(time)) or (clock != "HOURGLASS" and shout != int(time)):    
        print(shout, "NO")
    # 시간 역행의 법칙
    elif clock == "HOURGLASS":   
        print(shout, "NO")
        direction = changeDirection(direction)
    # 동기화의 법칙
    else:   
        print(shout, "YES")

    shout = (shout + direction) % 12
    if shout == 0:
        shout = 12

        