for _ in range(int(input())):
    n = int(input())
    rainbow = [1, 2, 3, 4, 5, 6, 7]
    l = list(map(int, input().split()))
    li = set(l)
    if l == l[::-1] and sorted(li) == rainbow:
        print("yes")
    else:
        print("no")