import copy

def solution(str1, str2):
    a = []
    b = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            a.append((str1[i] + str1[i + 1]).lower())

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            b.append((str2[i] + str2[i + 1]).lower())

    b_copy = copy.deepcopy(b)
    common  = 0
    for x in a:
        if x in b_copy:
            common += 1
            b_copy.remove(x)

    union = len(a) + len(b) - common
    
    if common == 0 and union == 0:
        answer = 1
    elif union == 0:
        answer = 0
    else:
        answer = common / union

    return int(answer * 65536)
