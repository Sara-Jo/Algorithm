from itertools import combinations_with_replacement

def solution(n, info):
    max_score_gap = 0
    for combi in combinations_with_replacement(range(11), n):
        ryan_info = [0] * 11
        for i in combi:
            ryan_info[10-i] += 1
            
        apeach, ryan = 0, 0
        for i in range(11):
            if info[i] == ryan_info[i] == 0:
                continue
            elif info[i] >= ryan_info[i]:
                apeach += 10 - i
            else:
                ryan += 10 - i
                
        if ryan > apeach and ryan - apeach > max_score_gap:
            max_score_gap = ryan - apeach
            answer = ryan_info
            
    if max_score_gap == 0:
        answer = [-1]
        
    return answer
            