s = input()
n = int(input())
for i in range(n):
    w = input()
    cnt = []
    for i in w:
        if i in s:
            cnt.append("yes")
        else:
            cnt.append("no")
    if "no" not in cnt:
        print("Yes")
    else:
        print("No")