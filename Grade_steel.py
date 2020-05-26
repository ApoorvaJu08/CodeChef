for _ in range(int(input())):
    hardness, cc, ts = map(float, input().split())
    hardness_check = hardness > 50
    cc_check = cc < 0.7
    ts_check = ts > 5600
    if hardness_check and cc_check and ts_check:
        grade = 10
    elif hardness_check and cc_check and (not ts_check):
        grade = 9
    elif (not hardness_check) and cc_check and ts_check:
        grade = 8
    elif hardness_check and (not cc_check) and ts_check:
        grade = 7
    elif int(hardness_check) + int(cc_check) + int(ts_check) == 1:
        grade = 6
    else:
        grade = 5
    print(grade)