from collections import Counter

r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))


def calculate_r():
    max_m = 0
    m = len(arr)
    for i in range(m):
        row = [num for num in arr[i] if num != 0]
        row = Counter(row).most_common()    # 각 숫자의 갯수 세기(리스트로 반환하기 위해 most_common 적용)
        row.sort(key=lambda x: (x[1], x[0]))    # 개수가 적은 순서부터 정렬, 개수가 같다면 작은 수부터
        arr[i] = []
        for num, count in row:
            arr[i].append(num)
            arr[i].append(count)
        max_m = max(max_m, len(arr[i]))
    
    # 가장 큰 행을 기준으로 0 채워주기
    for i in range(m):
        if len(arr[i]) < max_m:
            for _ in range(max_m - len(arr[i])):
                arr[i].append(0)
            arr[i] = arr[i][:100]

for second in range(101):
    m = len(arr)
    n = len(arr[0])

    if m >= r and n >= c and arr[r - 1][c - 1] == k:
        print(second)
        break

    if m >= n:
        calculate_r()
    else:
        arr = list(zip(*arr))
        calculate_r()
        arr = list(zip(*arr))
else:
    print(-1)