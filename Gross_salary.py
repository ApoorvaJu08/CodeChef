for _ in range(int(input())):
    x = int(input())
    if(x < 1500):
        print(x + (x * 0.10) + (x * 0.9))
    elif(x >= 1500):
        print(x + 500 + (x * 0.98))