n = int(input())
rings = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(1, n):
    gcd_num = gcd(rings[0], rings[i])
    print(f'{rings[0] // gcd_num}/{rings[i] // gcd_num}')