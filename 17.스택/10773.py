import sys
input = sys.stdin.readline

k = int(input())
nums = []
for _ in range(k):
    a = int(input())
    if a == 0:
        nums.pop()
    else:
        nums.append(a)

print(sum(nums))