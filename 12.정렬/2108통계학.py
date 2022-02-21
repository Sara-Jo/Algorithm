n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

def most_often(arr):
    max = 0
    for i in arr:
        cnt = arr.count(i)
        if max < cnt:
            max = cnt
    return max


arr.sort()
print(round(sum(arr) / n))  # 산술평균
print(arr[n // 2])  # 중앙값
print(most_often(arr))  # 최빈값
print(arr[n - 1] - arr[0])  # 범위