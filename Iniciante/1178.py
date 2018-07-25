X = float(input(''))
lista = list(range(100))


for y in range(100):
	if y == 0:
		X = X
		print('N[{}] = {:0.4f}'.format(lista[y],X))
	else:
		X = X/2
		print('N[{}] = {:0.4f}'.format(lista[y],X))