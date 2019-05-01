t = int(input().strip())
l = map(int, input().strip().split(" "))

evens = 0
odds = 0
for i in l:
    if i%2==0:
        evens += 1
    else:
        odds += 1
if evens > odds:
    print("READY FOR BATTLE")
else:
    print("NOT READY")