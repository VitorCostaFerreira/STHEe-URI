linha = int(input())
escolha = input()
matriz = list()
dados = list()
total = 0

for x in range(12):
    for y in range(12):
        dados.append(float(input()))
    matriz.append(dados[:])
    dados.clear()
    
for item in range(12):
    total += matriz[item][linha]
    
if escolha == 'S':
    print('{}'.format(total))
elif escolha == 'M':
    print('{:0.1f}'.format(total/12))