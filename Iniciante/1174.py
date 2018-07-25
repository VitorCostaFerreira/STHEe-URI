lista = list(range(100))

for i in range(0,len(lista)):
    lista[i] = float(input(''))
    if lista[i] <= 10:
        print('A[{}] = {}'.format(i,lista[i]))
    else:
        continue