for _ in range(int(input())):
    n = int(input())
    count = 0
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    for i in range(0,n):
        if(i==0):
            if(b[i]<= a[i]):
                count+=1
        else:
            if(b[i]<=(a[i]-a[i-1])):
                count+=1
    print(count)