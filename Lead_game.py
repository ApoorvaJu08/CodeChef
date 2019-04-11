# l1 = []
# l2 = []
# for i in range(int(input())):
#     x, y = map(int, input().split(' '))
#     if(y < x):
#         c = x - y
#         l1.append(c)
#     else:
#         d = y - x
#         l2.append(d)
#     x += x
#     y += y
# m = max(l1)
# n = max(l2)
# if(m > n):
#     print(1, m)
# else:
#     print(2, n)


games = int(input())
player1_score = 0
player2_score = 0
p1_wins = 0
p2_wins = 0
p1_greatest_lead = 0
p2_greatest_lead = 0
for game in range(games):
    scores = input()
    scores = scores.split()
    player1 = int(scores[0])
    player2 = int(scores[1])
    player1_score = player1_score + player1
    player2_score = player2_score + player2
    if player1_score > player2_score:
        p1_wins = p1_wins + 1
        lead = player1_score - player2_score
        if lead > p1_greatest_lead:
            p1_greatest_lead = lead
    else:
        p2_wins = p2_wins + 1
        lead = player2_score - player1_score
        if lead > p2_greatest_lead:
            p2_greatest_lead = lead

if p1_greatest_lead > p2_greatest_lead:
    print('1', p1_greatest_lead)
else:
    print('2', p2_greatest_lead)
