# def solution(N, stages):
#     answer = [] # 최종 리턴할 배열
#     data = []   # (실패율, 스테이지번호) 담긴 배열

#     stages.sort()

#     for i in range(N):
#         now = i + 1
#         fail_count = 0
#         reach_count = 0
#         for stage in stages:
#             if now == stage:
#                 fail_count += 1
#             if now <= stage:
#                 reach_count += 1
#         if reach_count == 0:
#             data.append([0, now])
#         else:
#             data.append([float(fail_count / reach_count), now])
        
#     data.sort(key=lambda x: (-x[0], x[1]))

#     for fails, stage in data:
#         if stage > N:
#             stage = N
#         answer.append(stage)

#     return answer

#------------------------------------------------------------------------

def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer