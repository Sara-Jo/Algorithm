# (시간 초과)
# def solution(enroll, referral, seller, amount):
#     result = [0] * len(enroll)

#     for i in range(len(seller)):
#         enroll_idx = enroll.index(seller[i])    # 해당 셀러의 인덱스
#         sales = amount[i] * 100
#         result[enroll_idx] += sales - int(sales * 0.1) # result에 매출액의 90% 더하기
#         rest = int(sales * 0.1)   # 매출액의 나머지 10%
#         while True:
#             if referral[enroll_idx] == '-':
#                 break
#             up_seller_idx = enroll.index(referral[enroll_idx])    # 추천인의 인덱스
#             result[up_seller_idx] += rest - int(rest * 0.1)
#             rest = int(rest * 0.1)
#             enroll_idx = up_seller_idx

#     return result


import math

def solution(enroll, referral, seller, amount):
    result = dict(zip(enroll, [0 for _ in range(len(enroll))]))
    tree = dict(zip(enroll, referral))

    for i in range(len(seller)):
        person = seller[i]
        sales = amount[i] * 100

        while True:
            if sales < 10:   #10원 단위 이하라면 모두 받고 레퍼럴 종료
                result[person] += sales
                break
            result[person] += math.ceil(sales * 0.9)
            if tree[person] == '-':
                break
            sales = math.floor(sales * 0.1)
            person = tree[person]

    return list(result.values())