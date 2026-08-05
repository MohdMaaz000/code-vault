A = set(input().split())
n = int(input())
is_strict_superset = True

for _ in range(n):
  other_set = set(input().split())
  if not (A > other_set):
    is_strict_superset = False
    break

print(is_strict_superset)
