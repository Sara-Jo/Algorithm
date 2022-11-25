import math

#(시간초과)
# def solution(n, stations, w):
#     answer = 0
#     wave = []

#     for station in stations:
#         wave.append(station)
#         for i in range(1, w + 1):
#             tmp = station + i
#             if tmp <= n:
#                 wave.append(tmp)
#             tmp = station - i
#             if tmp >= 1:
#                 wave.append(tmp)

#     length_list = []
#     length = 0
#     for i in range(1, n + 1):
#         if i not in wave:
#             length += 1
#         else:
#             if length != 0:
#                 length_list.append(length)
#                 length = 0
#     else:
#         length_list.append(length)

#     for l in length_list:
#         answer += math.ceil(l / (w * 2 + 1))

#     return answer



def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1

    start = 1
    for station in stations:
        answer += max(math.ceil((station - w - start) / W), 0)
        start = station + w + 1

    if n >= start:
        answer += math.ceil((n - start + 1) / W)

    return answer