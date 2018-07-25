def parimpar(resultado):

    if resultado%2 == 0:
        #PAR VENCE
        if entrada[1] == 'PAR':
            print(entrada[0])
        else:
            print(entrada[2])
    if resultado%2 != 0:
        if entrada[3] == 'IMPAR':
            print(entrada[2])
        else:
            print(entrada[0])

QT = int(input(''))

for i in range(1,QT+1):
    entrada = list(map(str, input('').split()))
    inteiros = list(map(int, input('').split()))

    resultado = inteiros[0] + inteiros[1]
    parimpar(resultado)
