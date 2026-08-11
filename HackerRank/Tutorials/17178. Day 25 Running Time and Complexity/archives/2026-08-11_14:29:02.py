import math

t = int(input())

for _ in range(t):
    n = int(input())

    if n < 2:
        print("Not prime")
        continue

    is_prime = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not prime")
