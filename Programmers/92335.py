def changeBase(n, k):
    temp = ""
    while n:
        temp += str(n % k)
        n //= k
    return temp[::-1]


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    if k != 10:
        n = changeBase(n, k)
    else:
        n = str(n) 
    
    arr = n.split('0')
    answer = 0
    for num in arr:
        if num != '' and isPrime(int(num)):
            answer += 1

    return answer


print(solution(3, 4))