# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[+-]?(\d*\.\d+)$'

for _ in range(int(input())):
    print(bool(re.match(pattern, input())))
