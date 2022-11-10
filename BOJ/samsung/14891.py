from collections import deque

gears = [[] for _  in range(5)]
for i in range(1, 5):
    gears[i] = deque(map(int, input()))

k = int(input())
moves = []
for _ in range(k):
    moves.append(list(map(int, input().split())))

def rotate_left(num, dir):
    # 왼쪽에 톱니바퀴가 없거나 맞닿은 톱니의 극이 같으면 중단
    if num < 1 or gears[num + 1][6] == gears[num][2]:
        return

    rotate_left(num - 1, -dir)  
    gears[num].rotate(dir)  

def rotate_right(num, dir):
    # 오른쪽에 톱니바퀴가 없거나 맞닿은 톱니의 극이 같으면 중단
    if num > 4 or gears[num - 1][2] == gears[num][6]:
        return

    rotate_right(num + 1, -dir)
    gears[num].rotate(dir)  

for num, dir in moves:
    rotate_left(num - 1, -dir)  # 왼쪽 톱니바퀴 확인(회전 방향은 반대로 설정)
    rotate_right(num + 1, -dir) # 오른쪽 톱니바퀴 확인(회전 방향은 반대로 설정)
    gears[num].rotate(dir)  # 톱니바퀴 회전

# 결과 출력
result = 0
for i in range(4):
    result += gears[i + 1][0] * (2 ** i)

print(result)