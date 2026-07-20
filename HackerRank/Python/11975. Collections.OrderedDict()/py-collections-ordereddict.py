from collections import OrderedDict

# Read total number of item lines
n = int(input())
item_sales = OrderedDict()

for _ in range(n):
    # Split input and isolate the price from multi-word item names
    data = input().rsplit(' ', 1)
    item_name, price = data[0], int(data[1])
    
    # Update the tracking history dictionary
    if item_name in item_sales:
        item_sales[item_name] += price
    else:
        item_sales[item_name] = price

# Print unique items in order of their first occurrence
for item_name, net_price in item_sales.items():
    print(f"{item_name} {net_price}")
