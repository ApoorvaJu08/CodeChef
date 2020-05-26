for _ in range(int(input())):
    string = input()
    a = set(string)
    l = []
    z = 0
    for i in a:
        x = string.count(i)
        l.append(x)
    y = max(l)
    l.remove(y)
    for j in l:
        z += j
    if y == z:
        print("YES")
    else:
        print("NO")