from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    l = len(queue1)

    answer = 0
    while True:
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum2 -= queue2[0]
            sum1 += queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1
        if answer >= l * 4:
            return -1
    