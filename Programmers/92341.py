import math

def solution(fees, records):
    in_cars = {}    # 현재 주차장에 있는 차
    durations = {}  # 차별 누적 주차 시간
    prices = {}  # 차별 누적된 요금
    
    for record in records:
        time, car, move = map(str, record.split())
        
        if move == "IN":
            in_cars[car] = time
            
        else:
            in_h, in_m = map(int, in_cars[car].split(':'))
            out_h, out_m = map(int, time.split(':'))
            
            del in_cars[car]
            
            # 주차 시간 구하기
            if out_m >= in_m:
                duration = (out_h - in_h) * 60 + (out_m - in_m)
            else:
                duration = (out_h - in_h - 1) * 60 + (out_m + 60 - in_m)
                
            if car in durations:
                durations[car] += duration
            else:
                durations[car] = duration
                
    for car in in_cars:
        in_h, in_m = map(int, in_cars[car].split(':'))
        duration = (23 - in_h) * 60 + (59 - in_m)
        if car in durations:
            durations[car] += duration
        else:
            durations[car] = duration
    
    # 요금 구하기
    for car in durations:
        if durations[car] > fees[0]:
            price = fees[1] + math.ceil((durations[car] - fees[0]) / fees[2]) * fees[3]
        else:
            price = fees[1]
        prices[car] = price
                
    prices = sorted(prices.items())
    answer = [price[1] for price in prices]
    return answer