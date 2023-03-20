from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    range_arr = [i for i in range(col)]

    # 모든 조합 구하기
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range_arr, i))

    # 유일성 검사
    unique = []
    for candidate in candidates:
        temp = [tuple(item[candi] for candi in candidate) for item in relation]
        if len(set(temp)) == row:
            unique.append(candidate)

    # 최소성 검사
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)