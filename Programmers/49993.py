def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        i = 0
        flag = True
        for x in skill_tree:
            if x not in skill:
                continue
            if x == skill[i]:
                i += 1
            else:
                flag = False
                break
        if flag == True:
            answer += 1

    return answer