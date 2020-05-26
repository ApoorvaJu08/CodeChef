for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print((n-1)*a[0])