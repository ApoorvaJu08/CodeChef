for _ in range(int(input())):
    n_n = int(input())
    n = list(map(int, input().split()))
    n_f = int(input())
    f = list(map(int, input().split()))
    if set(f).issubset(n):
        print("Yes")
    else:
        print("No")