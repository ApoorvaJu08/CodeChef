for _ in range(int(input())):
    n = int(input())
    s = input()
    s_list = list(s)
    count_list = []
    zero = 0
    count_list.append(s_list.count('R'))
    count_list.append(s_list.count('G'))
    count_list.append(s_list.count('B'))
    if s_list[1:] == s_list[:-1]:
        print(zero)
    else:
        print(n - max(count_list))
    