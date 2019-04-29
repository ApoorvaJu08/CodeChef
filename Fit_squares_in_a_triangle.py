T = int(input())

for t in range(0, T):
    B = int(input())
    B = int((B / 2) - 1)
    result = int(B * (B + 1) / 2)
    print(result)