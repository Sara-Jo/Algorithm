# 1 ---------------------------------------------
from selectors import EpollSelector


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

# count = {}
# for i in a:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# def binary_search(arr, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if arr[mid] == target:
#         return count.get(target)
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid + 1, end)
#     else:
#         return binary_search(arr, target, start, mid - 1)

# for i in b:
#     print(binary_search(a, i, 0, n - 1), end=' ')

# 3 ---------------------------------------------
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

# 4 ---------------------------------------------
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