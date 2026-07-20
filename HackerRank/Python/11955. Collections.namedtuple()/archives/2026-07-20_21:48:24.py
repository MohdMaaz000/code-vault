from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input().split())
students = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")
