t = int(input())
fact = 1

for i in range(0, t):
    n = int(input())
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
    fact = 1