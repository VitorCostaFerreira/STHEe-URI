try:
    N = int(input(''))
    cont = 0
    for i in range(1,N+1):
        X = int(input(''))
        for j in range(1,X+1):
            if X%j == 0:
                cont += 1
        if cont > 2:
            print('{} nao eh primo'.format(X))
            cont = 0
            continue
        if cont <= 2:
            print('{} eh primo'.format(X))
            cont = 0
            continue
except:
    vitor = 1