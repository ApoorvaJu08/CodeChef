price = [2**(i) for i in range(12)]
for i in range(int(input())):
    count = 0
    p = int(input())
    for j in price[-1::-1]:
        count += p//j
        p -= (j * (p//j))
    print(count)