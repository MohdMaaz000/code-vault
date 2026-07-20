from collections import Counter

# Read total number of shoes
num_shoes = int(input())

# Read shoe sizes and create the inventory counter
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

# Read number of customers
num_customers = int(input())

total_earned = 0

# Process each customer order
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # If the shoe size is available, sell it
    if inventory[size] > 0:
        total_earned += price
        inventory[size] -= 1  # Reduce stock by 1

# Output total earnings
print(total_earned)
