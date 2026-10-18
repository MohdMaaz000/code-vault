from collections import deque

d = deque()

for _ in range(int(input())):
    command = input().split()

    if len(command) == 2:
        getattr(d, command[0])(int(command[1]))
    else:
        getattr(d, command[0])()

print(*d)
