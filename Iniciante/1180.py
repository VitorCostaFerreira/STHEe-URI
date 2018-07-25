N = int(input(''))
menor = 0
lista = list(range(N))

lista = list(map(int, input('').split()))

for i in range(0,len(lista)):

    if lista[i] == 0:
        menor = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]
        else:
            continue
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(lista.index(menor)))