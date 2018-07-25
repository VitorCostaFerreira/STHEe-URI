coelhos = ratos = sapos = total = 0

n = int(input(''))

for i in range(0, n):
    entrada = list(map(str, input('').split()))
    ent = int(entrada[0])
    total += int(entrada[0])
    if entrada[1] == 'R':
        ratos += ent
    elif entrada[1] == 'S':
        sapos += ent
    elif entrada[1] == 'C':
        coelhos += ent
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))

print('Percentual de coelhos: {:0.2f} %'.format((coelhos/total)*100))
print('Percentual de ratos: {:0.2f} %'.format((ratos/total)*100))
print('Percentual de sapos: {:0.2f} %'.format((sapos/total)*100))