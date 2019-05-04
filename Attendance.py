def repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        for j in range(i+1, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

for _ in range(int(input())):
    fn, ln = [], []
    l, r = 0, []
    for i in range(int(input())):
        x, y = input().split(" ")
        fn.append(x)
        ln.append(y)
    r = repeat(fn)
    l = int(len(fn))
    for z in range(l):
        if(fn[z] in r):
            print(fn[z] + " "+ ln[z])
        else:
            print(fn[z])


    
    