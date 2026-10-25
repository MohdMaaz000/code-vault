N, X = map(int, input().split())

marks = [list(map(float, input().split())) for _ in range(X)]

for student in zip(*marks):
    average = sum(student) / X
    print(average)
