n = int(input(''))

for i in range(1, n+1):
    entrada = list(map(float, input('').split()))

    X = entrada[0]
    Y = entrada[1]

    try:
        resultado = X/Y
        print(resultado)
    except:
        print('divisao impossivel')