# -*- coding: utf8 -*- 
from collections import deque

n, m, k = map(int, input().split())
nutrients = [[5] * n for _ in range(n)]
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    # 봄: 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    for i in range(n):
        for j in range(n):
            len_trees = len(trees[i][j])
            for k in range(len_trees):
                # 땅의 양분이 부족하면 나무 죽음
                if nutrients[i][j] < trees[i][j][k]:
                    # 여름: 봄에 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
                    for _ in range(k, len_trees):                    
                        nutrients[i][j] += trees[i][j].pop() // 2
                    break
                else:
                    nutrients[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # 가을: 나이가 5의 배수인 나무와 인접한 8개의 칸에 나이가 1인 나무가 번식
    for i in range(n):
        for j in range(n):
            for k in trees[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1) # 나무가 항상 오름차순이 되도록

            # 겨울: 각 칸에 a[r][c]만큼 양분 추가
            nutrients[i][j] += a[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)