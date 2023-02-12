def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0 
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            answer += 5
        cache.append(city)
               
    return answer