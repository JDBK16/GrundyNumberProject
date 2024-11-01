def MinimumExcludent(S):
    min = 0
    while min in S:
        min += 1
    return min

S = {0, 1, 2, 3, 4, 5, 6, 7, 9}
print(MinimumExcludent(S))