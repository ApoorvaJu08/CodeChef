n = int(input())
for i in range(0, n):
    x, y = map(int, input().split(' '))
    a, b = divmod(x, y)
    print(b)