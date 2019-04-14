count = 0
for i in range(int(input())):
    t = int(input())
    for i in str(t):
        if(i == '4'):
            count += 1
    print(count)
    count = 0