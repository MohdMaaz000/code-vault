def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        score = n - i
        if string[i] in vowels:
            kevin += score
        else:
            stuart += score

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

