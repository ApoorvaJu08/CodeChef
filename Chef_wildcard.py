def check(str1, str2):
    for i in range(len(str1)):
        if str1[i] != '?' and str2[i] != '?' and str1[i] != str2[i]:
            return("No")
    return("Yes")

for _ in range(int(input())):
    str1 = input()
    str2 = input()
    print(check(str1, str2))