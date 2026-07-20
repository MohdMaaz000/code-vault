from collections import defaultdict

# Read the sizes of group A (n) and group B (m)
n, m = map(int, input().split())

# Create a defaultdict with a list factory to store 1-based indices
group_a_indices = defaultdict(list)

# Record the 1-based index for each word in group A
for index in range(1, n + 1):
    word = input().strip()
    group_a_indices[word].append(index)

# Check and print the indices for each word in group B
for _ in range(m):
    word = input().strip()
    if word in group_a_indices:
        print(*group_a_indices[word])
    else:
        print("-1")
