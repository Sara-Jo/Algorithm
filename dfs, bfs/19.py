# from itertools import permutations

# n = int(input())
# nums = list(map(int, input().split()))
# operators = list(map(int, input().split()))

# oper_data = []
# for i in range(4):
#     for j in range(operators[i]):
#         if i == 0:
#             oper_data.append('+')
#         if i == 1:
#             oper_data.append('-')
#         if i == 2:
#             oper_data.append('*')
#         if i == 3:
#             oper_data.append('/')

# candidates = list(permutations(oper_data, n - 1))

# max_result = -1e9
# min_result = 1e9

# def calculate(n, nums, candidate):
#     result = nums[0]
#     for i in range(1, n):
#         if candidate[i - 1] == '+':
#             result += nums[i]
#         if candidate[i - 1] == '-':
#             result -= nums[i]
#         if candidate[i - 1] == '*':
#             result *= nums[i]
#         if candidate[i - 1] == '/':
#             if result < 0:
#                 result = -result
#                 result //= nums[i]
#                 result = -result
#             else:
#                 result //= nums[i]
#     return result

# for candidate in candidates:
#     ret = calculate(n, nums, candidate)
#     max_result = max(max_result, ret)
#     min_result = min(min_result, ret)

# print(max_result)
# print(min_result)

#--------------------------------------------------------------------

# n = int(input())
# # 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())

# # 최솟값과 최댓값 초기화
# min_value = 1e9
# max_value = -1e9

# # 깊이 우선 탐색(DFS) 메서드
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         # 각 연산자에 대하여 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i]))  # 나눌 때는 나머지를 제거
#             div += 1

# # DFS 메서드 호출
# dfs(1, data[0])

# # 최댓값과 최솟값 차례대로 출력
# print(max_value)
# print(min_value)

#--------------------------------------------------------------------

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def f(num, index, add, sub, mul, div):
    global max_value, min_value
    if index == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    if add > 0:
        f(num + nums[index], index + 1, add - 1, sub, mul, div)
    if sub > 0:
        f(num - nums[index], index + 1, add, sub - 1, mul, div)
    if mul > 0:
        f(num * nums[index], index + 1, add, sub, mul - 1, div)
    if div > 0:
        f(int(num / nums[index]), index + 1, add, sub, mul, div - 1)

f(nums[0], 1, add, sub, mul, div)

print(max_value)
print(min_value)
    