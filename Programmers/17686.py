def solution(files):
    arr = []
    for k in range(len(files)):
        i = 0
        while not files[k][i].isdigit():
            i += 1
        head = files[k][:i]
        j = i
        while j < len(files[k]) and files[k][j].isdigit():
            j += 1
        num = files[k][i:j]
        arr.append((head.lower(), int(num), k, files[k]))
    arr = sorted(arr)
    
    answer = []
    for file in arr:
        answer.append(file[3])
        
    return answer