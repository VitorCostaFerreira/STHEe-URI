n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
n4 = int(input(''))
n5 = int(input(''))

entrada = [n1,n2,n3,n4,n5]

pares = impares = 0
for i in range(0,5):
    if entrada[i]%2 == 0:
        pares += 1
    else:
        impares += 1
print('{} valores pares'.format(pares))