tests = int(input())
for test in range(tests):
    greatest_profit = 0
    coins, people = map(int, input().split())
    for person in range(1, people + 1):
        profit = coins % person
        if profit > greatest_profit:
            greatest_profit = profit
    print(greatest_profit)