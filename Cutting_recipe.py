import math as m
for _ in range(int(input())):
    n=list(map(int,input().split()))
    gcd=n[1]
    for i in range(2,n[0]+1):
        gcd=m.gcd(gcd,n[i])
        
    for j in range(1,len(n)):
        print(n[j]//gcd ,end=" ")
