nome = input('')
fixo = float(input(''))
venda = float(input(''))
bonus = venda*0.15
total = fixo+bonus
print('TOTAL = R$ {:0.2f}'.format(total))