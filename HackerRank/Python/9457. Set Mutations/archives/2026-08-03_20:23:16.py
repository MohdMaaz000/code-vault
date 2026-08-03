n = int(input())
A = set(map(int, input().split()))
num_operations = int(input())


for _ in range(num_operations):
  op_details = input().split()
  op_name = op_details[0]
  other_set = set(map(int, input().split()))

  getattr(A, op_name)(other_set)

print(sum(A))
