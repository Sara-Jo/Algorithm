# def solution(A, B):
#     A.sort()
#     B.sort()

#     result = 0
#     j = 0
#     for i in range(len(A)):
#         if j >= len(B):
#             break
#         while A[i] >= B[j] and j < len(B) - 1:
#             j += 1
#         if A[i] < B[j]:
#             result += 1
#             j += 1
    
#     return result


def solution(A, B):
    result = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            result += 1
            j += 1

    return result