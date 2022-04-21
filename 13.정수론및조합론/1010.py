# 1 ---------------------------------------------
d = [0] * 30
d[1] = 1
d[2] = 2
for i in range(3, 30):
    d[i] = i * d[i - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(1)
        continue
    print(d[m] // d[m - n] // d[n])

# 2 ---------------------------------------------
# def factorial(x):
#     result = 1
#     for i in range(1, x + 1):
#         result *= i
#     return result

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     print(factorial(m) // factorial(m - n) // factorial(n))

# 3 ---------------------------------------------
# from math import factorial

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     print(factorial(m) // factorial(m - n) // factorial(n))