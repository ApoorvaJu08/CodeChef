for _ in range(int(input())):
    l = []
    for i in range(int(input())):
        x = int(input())
        l.append(x)
    a = set(l)
    for j in a:
        k = l.count(j)
        if k % 2 != 0:
            print(j)