A = int(input(''))
B = int(input(''))
C = int(input(''))
D = int(input(''))
E = int(input(''))
lista = [0,1,2,3,4]
lista[0] = A
lista[1] = B
lista[2] = C
lista[3] = D
lista[4] = E
impar = positivos = negativos = pares = 0
for i in range(0, len(lista)):
	if (lista[i] == 0):
		pares += 1
	elif (lista[i]%2 == 0) and (lista[i] > 0):
		pares += 1
		positivos += 1
	elif (lista[i]%2 != 0) and (lista[i] < 0):
		impar += 1
		negativos += 1
	elif (lista[i]%2 == 0) and (lista[i] < 0):
		pares += 1
		negativos += 1
	elif (lista[i]%2 != 0) and (lista[i] > 0):
		impar += 1 
		positivos += 1
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivos))
print('{} valor(es) negativo(s)'.format(negativos))
