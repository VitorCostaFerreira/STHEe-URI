L = int(input(''))
outra = input('')

dados = list()
matriz = list()
final = 0.0

for i in range(12):
    for j in range(12):
        if i == L:
            final += float(input(''))
        else:
            dados.append(float(input('')))
    matriz.append(dados[:])
    dados.clear()

if outra == 'S':
    print(final)
elif outra == 'M':
    final = final/12
    print(final)
