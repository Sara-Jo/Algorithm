from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    candidates = list(product(discounts, repeat=len(emoticons)))
    answer = []
    
    for candidate in candidates:
        discounted = []
        for i in range(len(emoticons)):
            discounted.append(emoticons[i] - (emoticons[i] * candidate[i] // 100))
        
        result = [0, 0]
        for user in users:
            price = 0
            for i in range(len(discounted)):
                if candidate[i] >= user[0]:
                    price += discounted[i]
            if price >= user[1]:
                result[0] += 1
            else:
                result[1] += price
        answer.append(result)
        
    return sorted(answer)[-1]