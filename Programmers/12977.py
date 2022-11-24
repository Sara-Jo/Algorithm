from itertools import combinations

def solution(nums):
    answer = 0

    candidates = combinations(nums, 3)
    for candidate in candidates:
        total = sum(candidate)
        flag = True
        for i in range(2, total // 2):
            if total % i == 0:
                flag = False
        if flag == True:
            answer += 1

    return answer