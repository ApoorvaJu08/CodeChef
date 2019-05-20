for _ in range(int(input())):
    n, m, k = map(int, input().split())
    difference = abs(n - m)
    if k >= difference:
        new_difference = 0
    else:
        new_difference = difference - k
    print(new_difference)