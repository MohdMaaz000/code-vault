# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read the space-separated elements for list A and list B
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the cartesian product of lists A and B
cartesian_product = product(A, B)

# Print the resulting tuples as space-separated items
print(*cartesian_product)
