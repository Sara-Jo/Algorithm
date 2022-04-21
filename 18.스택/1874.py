n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

index = 0
stack = []
print_arr = []
for i in arr:
    if i > index:
        while i != index:
            print_arr.append('+')
            index += 1
            stack.append(index)
    if i == stack[-1]:
        print_arr.append('-')
        stack.pop()
        continue
    print_arr.append('NO')
    break

if 'NO' in print_arr:
    print('NO')
else:
    for i in print_arr:
        print(i)
    