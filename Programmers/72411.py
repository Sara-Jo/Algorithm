from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []     
    for c in course:
        candidates = []
        for order in orders:
            l = list(combinations(sorted(order), c))
            candidates.extend(l)
            
        counter = Counter(candidates)
        if len(counter) > 0 and max(counter.values()) >= 2:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)