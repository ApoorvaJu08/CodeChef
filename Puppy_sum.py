for _ in range(int(input())):
    sum = 0
    D, N = map(int, input().split())
    for i in range(D):
        sum = 0
        for j in range(N+1):
            sum = sum + j
        N = sum
    print(sum)