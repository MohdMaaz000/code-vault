import re

for _ in range(int(input())):
    s = input()
    try:
        re.compile(s)
        if re.search(r'(?<!\\)[+*?]\+', s):
            print("False")
        else:
            print("True")
    except re.error:
        print("False")
