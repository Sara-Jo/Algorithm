s = list(input())

def countFlips(s, x):
    result = 0
    flag = 0
    for num in s:
        if num == x and flag == 0:
            result += 1
            flag = 1
        elif num != x:
            flag = 0
    return result

result1 = countFlips(s, '0')
result2 = countFlips(s, '1')

print(min(result1, result2))