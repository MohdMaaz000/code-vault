import math

a = int(input())
b = int(input())

angle = math.degrees(math.atan(a / b))

print(str(round(angle)) + chr(176))
