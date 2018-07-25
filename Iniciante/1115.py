for i in range(0,999999999999999):
    entrada = list(map(int, input('').split()))

    X = entrada[0]
    Y = entrada[1]

    if X > 0 and Y > 0:
        print('primeiro')
    elif X > 0 and Y < 0:
        print('quarto')
    elif X < 0 and Y > 0:
        print('segundo')
    elif X < 0 and Y < 0:
        print('terceiro')
    if X == 0 or Y == 0:
        quit()