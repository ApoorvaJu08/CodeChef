def answer():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        a = input()
        ans ^= i
    print(ans)

for _ in range(int(input())):
    answer()