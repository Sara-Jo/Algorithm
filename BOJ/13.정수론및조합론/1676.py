# 1 ---------------------------------------------
from math import factorial

n = int(input())
a = str(factorial(n))
cnt = 0
for i in range(len(a) - 1, -1, -1):
    if a[i] == '0':
        cnt += 1
    else:
        break
print(cnt)

# 2 ---------------------------------------------
# n = int(input())

# cnt = 0
# while n > 0:
#     cnt += n // 5
#     n //= 5

# print(cnt)