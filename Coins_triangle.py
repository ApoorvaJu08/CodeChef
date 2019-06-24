def coinTriangle(n):
    for i in range(1,n+2):
        x=(i*(i+1))/2
        if x>n:
            return i-1
            
for _ in range(int(input())):
    n=int(input())
    print(coinTriangle(n))