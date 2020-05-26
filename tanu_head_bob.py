for _ in range(int(input())):
    x = int(input())
    string = input()
    if string.find("I") != -1:
        print("INDIAN")
    elif string.find("Y") != -1:
        print("NOT INDIAN")
    else:
        print("NOT SURE")