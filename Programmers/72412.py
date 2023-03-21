from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    dict = {}
    for i in info:
        i = i.split()
        condition = i[:4]
        score = int(i[4])
        for j in range(5):
            combination = list(combinations([0, 1, 2, 3], j))
            for combi in combination:
                temp = condition[:]
                for c in combi:
                    temp[c] = '-'
                key = ''.join(temp)
                if key in dict:
                    dict[key].append(score)
                else:
                    dict[key] = [score]
                
    for k in dict:
        dict[k].sort()
    
    answer = []
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        condition = q[:4]
        score = int(q[4])
        
        count = 0
        key = ''.join(condition)
        if key in dict:
            idx = bisect_left(dict[key], score)
            count = len(dict[key]) - idx
        answer.append(count)
    
    return answer
