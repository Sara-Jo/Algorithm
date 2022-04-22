n, k = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = []

tmp = 0
for i in nums:
    tmp += i
    prefix_sum.append(tmp)

result = [prefix_sum[k - 1]]
for i in range(k, n):
    result.append(prefix_sum[i] - prefix_sum[i - k])

print(max(result))