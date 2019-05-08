


t = int(input())
for _ in range(t):
    n = int(input())
    n = n**2
    x1,y1 = [int(p) for p in input().split()]
    x2,y2 = [int(p) for p in input().split()]
    x3,y3 = [int(p) for p in input().split()]
    temp1 = ((x1-x2)**2)+((y1-y2)**2)
    temp2 = ((x2-x3)**2)+((y2-y3)**2)
    temp3 = ((x3-x1)**2)+((y3-y1)**2)
    #print(temp1,temp2,temp3,'ss',n)
    if( temp1 >n and temp2 > n) or( temp1 >n and temp3 > n) or ( temp3 >n and temp2 > n):
        print('no')
    else:
        print('yes')