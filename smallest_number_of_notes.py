notes = [1, 2, 5, 10, 50, 100]
for i in range(int(input())):
    count = 0
    price = int(input())
    for j in notes[-1::-1]:
        count += price//j
        price -= (j * (price//j))
    print(count)