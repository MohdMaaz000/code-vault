# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    # Read size and elements of the first set
    m = int(input())
    set_a = set(map(int, input().split()))
    
    # Read size and elements of the second set
    n = int(input())
    set_b = set(map(int, input().split()))
    
    # Calculate symmetric difference and sort it in ascending order
    sym_diff = sorted(set_a.symmetric_difference(set_b))
    
    # Print each element on a new line
    for element in sym_diff:
        print(element)
