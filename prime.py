for i in range(int(input())):
    x = int(input())
    count = 0
    if(x > 1):
        for j in range(2, x):
            if((x%j) == 0):
                count = 1
            else:
                continue
        if(count == 1):
            print("no")
        else:
            print("yes")