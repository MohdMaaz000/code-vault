from itertools import permutations

s, r = input().split()
r = int(r)

for p in permutations(sorted(s), r):
    print(''.join(p))
