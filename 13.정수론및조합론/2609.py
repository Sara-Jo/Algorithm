# 1 ---------------------------------------------
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(gcd(a, b))
print(a * b // gcd(a, b))

# 2 ---------------------------------------------
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))