n=int(input())
x=[]
for i in range(0,n):
    x.append(int(input()))
x.sort()
l=len(x)
for i in range (0,l):
    print(x[i])