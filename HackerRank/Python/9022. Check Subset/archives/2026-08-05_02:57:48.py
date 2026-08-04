num_test_cases = int(input())

for _ in range(num_test_cases):
    size_a = int(input())
    set_a = set(map(int, input().split()))
    
    size_b = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))
