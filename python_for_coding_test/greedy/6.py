# def solution(food_times, k):
#     answer = 0
    
#     while k > 0:
#         if sum(food_times) == 0:
#             break
#         while food_times[answer] == 0:
#             if answer == len(food_times) - 1:
#                 answer = 0
#             else:
#                 answer += 1
#         food_times[answer] -= 1
#         if answer == len(food_times) - 1:
#             answer = 0
#         else:
#             answer += 1
#         k -= 1
    
#     return answer + 1

# 채점 결과
# 정확성: 22.8
# 효율성: 0.0
# 합계: 22.8 / 100.0

# -------------------------------------------------------

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key =lambda x: x[1])
    return result[(k - sum_value) % length][1]

# 채점 결과
# 정확성: 42.9
# 효율성: 57.1
# 합계: 100.0 / 100.0