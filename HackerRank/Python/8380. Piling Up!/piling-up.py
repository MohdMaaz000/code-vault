from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))

    top = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube > top:
            print("No")
            break

        top = cube
    else:
        print("Yes")
