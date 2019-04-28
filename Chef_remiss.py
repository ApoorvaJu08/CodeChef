for i in range(int(input())):
    minimum, maximum = 0, 0
    a, b = map(int, input().split())
    minimun = max(a, b)
    maximum = (a + b)
    print(minimun, maximum)