# 1 ---------------------------------------------
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

tab = [0] * 20000001

for i in a:
    tab[i] += 1

for i in b:
    print(tab[i], end=' ')

# 2 ---------------------------------------------
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# m = int(input())
# b = list(map(int, input().split()))

# dic = dict()

# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# for i in range(m):
#     if b[i] in dic:
#         print(dic[b[i]], end=' ')
#     else:
#         print(0, end=' ')

# 3 ---------------------------------------------
# from collections import Counter

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# count = Counter(a)

# for i in range(len(b)):
#     if b[i] in count:
#         print(count[b[i]], end=' ')
#     else:
#         print(0, end=' ')