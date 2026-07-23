import sys

n = int(input())
phone_book = {}

for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

for query in sys.stdin:
    query = query.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
