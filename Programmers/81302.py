def solution(places):
    answer = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for place in places:
        should_break = False
        # graph 저장
        graph = []
        for row in place:
            graph.append(row)
        
        # 탐색
        for x in range(5):
            for y in range(5):
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if graph[x][y] == 'P' and graph[nx][ny] == 'P': # 응시가자 붙어있는 경우
                            answer.append(0)
                            should_break = True
                            break
                        elif graph[x][y] == 'O' and graph[nx][ny] == 'P':
                            count += 1
                            if count >= 2:
                                answer.append(0)
                                should_break = True
                                break
                            
                if should_break:
                        break
            if should_break:
                        break
        if not should_break:
            answer.append(1)
    
    return answer