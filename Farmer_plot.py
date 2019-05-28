from math import gcd
for _ in range(int(input())):
    N, M = map(int, input().split())
    k = gcd(N, M)
    N = N//k
    M = M//k
    print(N*M)