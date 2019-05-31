for _ in range(int(input())):
    N, K = map(int, input().split())
    N_words = [N_words for N_words in input().split()]
    phrase_list = []
    for i in range(K):
        phrase = [phrase for phrase in input().split()]
        k_no = phrase[0]
        phrase.remove(k_no)
        phrase_list.extend(phrase) 
    for i in N_words:
        if i in phrase_list:
            print("YES", end = ' ')
        else:
            print("NO", end = ' ')
    print()