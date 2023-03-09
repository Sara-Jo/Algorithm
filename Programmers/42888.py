def solution(record):
    answer = []
    nicknames = {}
    
    for x in record:
        if x[:5] == "Enter" or x[:6] == "Change":
            move, uid, nickname = map(str, x.split())
            nicknames[uid] = nickname

    for x in record:
        if x[:5] == "Enter":
            move, uid, nickname = map(str, x.split())
            message = nicknames[uid]
            message += "님이 들어왔습니다."
            answer.append(message)
        if x[:5] == "Leave":
            move, uid = map(str, x.split())
            message = nicknames[uid]
            message += "님이 나갔습니다."
            answer.append(message)
    
    return answer