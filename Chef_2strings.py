for _ in range(int(input())):
    str1 = input()
    str2 = input()
    min1, max1 = 0, 0
    for i in range(len(str1)):
        if str1[i] == '?' or str2[i] == '?' or str1[i] != str2[i] : max1 = max1 + 1
        if str1[i] != "?" and str2[i] != '?' and str1[i] != str2[i] : min1 = min1 + 1
    print("%d %d" % (min1, max1))