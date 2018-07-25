def teste():
    #final = []

    X = int(input(''))
    entrada = list(map(int, input('').split()))
    for i in range(0,X):
        if entrada[i] <= 10:
            entrada[i] = 1
        elif 10 < entrada[i] < 20:
            entrada[i] = 2
        elif entrada[i] >= 20:
            entrada[i] = 3
    fim = sorted(entrada)
    final = fim[::-1]
    if final[0] == 3:
        print('3')
    elif final[0] == 2:
        print('2')
    elif final[0] == 1:
        print('1')
try:
    while True:
        teste()
except EOFError:
    quit()