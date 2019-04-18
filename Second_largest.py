for i in range(int(input())):
    l = []
    maximum = 0
    second_maximum = 0
    a, b, c = map(int, input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    maximum = max(l)
    l.remove(maximum)
    second_maximum = max(l)
    print(second_maximum)