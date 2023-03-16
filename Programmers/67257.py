from itertools import permutations

def solution(expression): 
    
    def calculate(num1, oper, num2):
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        
    
    operators = set()   # 등장한 연산자
    arr = []    # expression을 숫자/연산자 단위로 쪼개서 저장
    count = 0   # 숫자 길이 체크
    start = 0   # 숫자가 시작되는 인덱스 체크
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            arr.append(int(expression[start:i])) # 숫자 담기
            arr.append(expression[i])   # 연산자 담기
            operators.add(expression[i])    # 연산자 담기
            count = 0
            start = i + 1
        else:
            count += 1
    arr.append(int(expression[start:len(expression)]))
                             
    candidates = list(permutations(operators, len(operators)))  # 연산자 우선순위 후보
    answer = 0
    for candidate in candidates:
        arr_copy = arr[:]
        for operator in candidate:
            remove_count = 0
            for i in range(len(arr_copy)):
                if arr_copy[i] == operator:
                    temp = calculate(arr_copy[i-1], arr_copy[i], arr_copy[i+1])
                    arr_copy[i+1] = temp
                    arr_copy[i-1], arr_copy[i] = 'X', 'X'
                    remove_count += 2
            for _ in range(remove_count):
                arr_copy.remove('X')
                    
        answer = max(answer, abs(arr_copy[0]))

    return answer