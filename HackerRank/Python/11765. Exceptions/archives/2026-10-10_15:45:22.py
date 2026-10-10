for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
