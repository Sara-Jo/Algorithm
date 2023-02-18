def changeBase(base, num):
    if num == 0:
        return '0'
    
    baseChr = "0123456789ABCDEF"
    answer = ""
    while num:
        d, m = divmod(num, base)
        answer += baseChr[m]
        num = d
    return answer[::-1]
    

def solution(n, t, m, p):
    game = ""
    for i in range(t * m):
        game += changeBase(n, i)
    
    answer = ""
    for _ in range(t):
        answer += game[p - 1]
        p += m
    
    return answer