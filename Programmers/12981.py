# def solution(n, words):
#     arr = [[] for _ in range(n + 1)]
#     arr[1].append(words[0])
#     person = 1
#     prev = words[0][-1]
#     word_check = [words[0]]
#     flag = True

#     for i in range(1, len(words)):
#         if person == n:
#             person = 1
#         else:
#             person += 1
#         arr[person].append(words[i])
#         if prev != words[i][0] or words[i] in word_check:
#             flag = False
#             break
#         word_check.append(words[i])
#         prev = words[i][-1]

#     if flag == True:
#         return 0, 0
#     else:
#         return [person, len(arr[person])]



def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            return [(i % n) + 1, (i // n) + 1]
    else:
        return [0, 0]