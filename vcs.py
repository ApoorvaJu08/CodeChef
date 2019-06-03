for _ in range(int(input())):
    n, m, k = map(int, input().split())
    ignored = [int(ignored) for ignored in input().split()]
    tracked = [int(tracked) for tracked in input().split()]
    count_tracked_ignored, count_untracked_unignored = 0, 0
    for i in ignored:
        if i in tracked:
            count_tracked_ignored += 1
    for j in range(1, n+1):
        if ((j not in ignored) and (j not in tracked)):
            count_untracked_unignored += 1
    print(str(count_tracked_ignored) + " " + str(count_untracked_unignored))