for _ in range(int(input())):
    sum = 0.0
    quantity, price = map(int, input().split())
    sum = quantity*price
    if(quantity > 1000):
        print("{:6f}".format(sum - (sum * 0.1)))
    else:
        print("{:6f}".format(sum))