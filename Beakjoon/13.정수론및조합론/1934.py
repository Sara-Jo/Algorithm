# 1 ---------------------------------------------
t = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))

# 2 ---------------------------------------------
# import math

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print(math.lcm(a, b))