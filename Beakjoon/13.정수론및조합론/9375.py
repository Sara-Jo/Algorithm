# 1 ---------------------------------------------
t = int(input())

for _ in range(t):
    n = int(input())
    arr = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if b in arr:
            arr[b] += 1
        else:
            arr[b] = 1
    
    cnt = 1
    for i in arr:
        cnt *= arr[i] + 1

    print(cnt - 1)

# 2 ---------------------------------------------
# from collections import Counter

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = []
#     for _ in range(n):
#         a, b = map(str, input().split())
#         arr.append(b)

#     result = Counter(arr)
#     cnt = 1
#     for i in result:
#         cnt *= result[i] + 1
    
#     print(cnt - 1)