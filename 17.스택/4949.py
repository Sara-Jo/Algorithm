a = list(input())
arr = []
while a != ['.']:
    arr.append(a)
    a = list(input())

for i in arr:
    stack = []
    for j in i:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break
        elif j == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(j)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')