for _ in range(int(input())):
    l=[]
    n=int(input())
    for i in range(n):
        l.append([int(x) for x in input().split()])
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            l[i][j]+=(max(l[i+1][j],l[i+1][j+1]))
    print(l[0][0])