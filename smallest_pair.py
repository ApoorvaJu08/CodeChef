for i in range(int(input())):
    x = int(input())
    l = list(map(int, input().strip().split(" ")))
    l.sort()
    print(l[0] + l[1])
    # l1 = []
    # for j in l:
    #     for k in l[j+1:]:
    #         s = j+k 
    #         l1.append(s)
    # print(min(l1))