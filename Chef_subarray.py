for _ in range(int(input())):
    n = int(input())
    count = 0
    l = list(map(int, input().split()))
    for i in range(0, n):
        for j in range(i, n):
            s, p = 0, 1 
            for k in range(i, j+1):
                s += l[k]
                p *= l[k]
            if s == p:
                count += 1
    print(count)