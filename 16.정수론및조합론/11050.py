# 1 ---------------------------------------------
n, k = map(int, input().split())
result = 1
for i in range(k):
    result *= n - i
for i in range(1, k + 1):
    result //= i
print(result)

# 2 ---------------------------------------------
# from math import factorial

# n, k = map(int, input().split())
# print(factorial(n) // (factorial(k) * factorial(n - k)))