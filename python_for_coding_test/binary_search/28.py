n = int(input())
nums = list(map(int, input().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (end + start) // 2
        if array[mid] == mid:
            return mid
        if array[mid] < mid:
            start = mid + 1
        else: 
            end = mid - 1
    return None

result = binary_search(nums, 0, len(nums) - 1)

if result == None:
    print(-1)
else:
    print(result)
