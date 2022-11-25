def solution(survey, choices):
    data = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        if choices[i] in [1, 2, 3]:
            data[survey[i][0]] += -choices[i] + 4
        elif choices[i] in [5, 6, 7]:
            data[survey[i][1]] += choices[i] - 4

    answer = ''
    if data['R'] >= data['T']:
        answer += 'R'
    else:
        answer += 'T'

    if data['C'] >= data['F']:
        answer += 'C'
    else:
        answer += 'F'

    if data['J'] >= data['M']:
        answer += 'J'
    else:
        answer += 'M'

    if data['A'] >= data['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer