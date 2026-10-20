from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combos = list(combinations(letters, k))
count = sum('a' in combo for combo in combos)

probability = count / len(combos)
print(f"{probability:.4f}")
