A = float(input(''))
B = float(input(''))
C = float(input(''))
D = float(input(''))
E = float(input(''))
F = float(input(''))

lista = [A,B,C,D,E,F]

positivos = 0

for i in range(0, len(lista)):
	if lista[i] > 0:
		positivos += 1
print('{} valores positivos'.format(positivos))