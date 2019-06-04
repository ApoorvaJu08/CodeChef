for _ in range(int(input())):
    x = [int(x) for x in input().split()]
    x1 = x[0]
    y1 = x[1]
    x2 = x[2]
    y2 = x[3]
    if x1 != x2 and y1 != y2:
        print("sad")
    else:
        if x1 == x2:
            if y2 > y1:
                print("up")
            else:
                print("down")
        elif y1 == y2:
            if x2 > x1:
                print("right")
            else:
                print("left")