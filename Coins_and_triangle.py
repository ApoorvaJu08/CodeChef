for _ in range(int(input())):
    n = int(input())
    i, h = 1, 0
    while n > 0:
        n -= i
        if(n >= 0):
            h += 1
        i += 1
    print(h)