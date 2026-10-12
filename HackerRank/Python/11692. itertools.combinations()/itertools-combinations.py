from itertools import combinations

s, k = input().split()
s = sorted(s)

for r in range(1, int(k) + 1):
    for comb in combinations(s, r):
        print(''.join(comb))
