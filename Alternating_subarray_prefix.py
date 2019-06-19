for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l1 = [-1]*n
    l1[-1] = 1
    for i in range(n-2, -1, -1):
        if((l[i]*l[i+1]) < 0):
            l1[i] = l1[i+1] + 1
        else:
            l1[i] = 1
    for i in range(n):
        print(l1[i], end = ' ')