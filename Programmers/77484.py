def solution(lottos, win_nums):
    answer = []

    cnt = 0 # 일치하는 번호의 개수
    zeros = 0   # 알아볼 수 없는 번호의 개수
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            zeros += 1

    # 최고 순위: 알아볼 수 없는 번호가 모두 일치하는 번호인 경우
    if cnt + zeros == 0:
        answer.append(6)
    else:
        answer.append(7 - (cnt + zeros))

    # 최저 순위: 알아볼 수 없는 번호가 모두 일치하지 않는 번호인 경우
    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7 - cnt)

    return answer

#-------------------------------------------------------------------

# def solution(lottos, win_nums):
#     rank = [6, 6, 5, 4, 3, 2, 1]

#     zeros = lottos.count(0)
#     answer = 0
#     for x in win_nums:
#         if x in lottos:
#             answer += 1
#     return rank[zeros + answer], rank[answer]