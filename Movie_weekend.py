for _ in range(int(input())):
    movies = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    max_list = []
    index_list = []
    maximum, index, index1, max_r = 0, 0, 0, 0
    for i in range(0, movies):
        p = l[i]*r[i]
        max_list.append(p)
    maximum = max(max_list)
    ind = max_list.index(maximum)
    if max_list.count(maximum) > 1:
        j= [x for x in range(len(max_list)) if(max_list[x]==maximum)]
        h = [r[x] for x in j]
        ma = max(h)
        index1 = r.index(ma)
        print(index1+1)
    else:
        print(ind+1)        
    
# import numpy as np
# for _ in range(int(input())):
#     n=int(input())
#     l=[int(x) for x in input().split()]
#     r=[int(x) for x in input().split()]
#     p=list(np.array(l)*np.array(r))
#     mi=max(p)
#     k1=list(filter(lambda x:x==mi,p))
#     if(len(k1)>1):
#         j=[x for x in range(len(p)) if(p[x]==mi)]
#         h=[r[x] for x in j]
#         ma=max(h)
#         i=r.index(ma)
#         print(i+1)
#     elif(len(k1)==1):
#         i=p.index(mi)
#         print(i+1)
        