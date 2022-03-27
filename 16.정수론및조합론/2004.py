n, m = map(int, input().split())

def count_num(a, b):
    cnt = 0
    while a > 0:
        cnt += a // b
        a //= b
    return cnt

five_count = count_num(n, 5) - count_num(n - m, 5) - count_num(m, 5)
two_count = count_num(n, 2) - count_num(n - m, 2) - count_num(m, 2)

print(min(five_count, two_count))