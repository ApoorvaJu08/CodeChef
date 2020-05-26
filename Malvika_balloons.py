for _ in range(int(input())):
    s = input()
    no_a, no_b = s.count('a'), s.count('b')
    print(min(no_a, no_b))
