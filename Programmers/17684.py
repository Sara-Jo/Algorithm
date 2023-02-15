def solution(msg):
    answer = []
    dict = {}

    max_dict = 27
    while True:
        w = ""
        # 현재 입력(w) 찾기
        for i in range(len(msg) + 1, -1, -1):
            if msg[0:i] in dict:
                w = msg[0:i]
                break
        else:
            w = msg[0]

        # 색인 번호 출력
        if len(w) == 1:
            answer.append(ord(w) - 64)
        else:
            answer.append(dict[w])

        # 입력에서 w 제거
        msg = msg[len(w):]

        if len(msg) == 0:
            break
        else:
            tmp = w + msg[0]
            dict[tmp] = max_dict
            max_dict += 1

    return answer