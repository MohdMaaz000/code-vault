# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top half
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, '-'))

# Middle
print("WELCOME".center(m, '-'))

# Bottom half
for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, '-'))
