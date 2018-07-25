while True:
    entrada = list(map(int, input('').split()))
    X = entrada[0]
    Y = entrada[1]
    if X == Y:
        break
    else:
        if X > Y:
            print('Decrescente')
        if Y > X:
            print('Crescente')