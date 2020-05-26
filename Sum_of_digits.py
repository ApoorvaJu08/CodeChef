def tot(n):
    m = 0
    while n:
        m += (n%10)
        n = n//10
    return m
x = []
y = []
for i in range(int(input())):
    x.append(int(input()))
for i in x:
    y.append(tot(i))
for i in y:
    print(i)
