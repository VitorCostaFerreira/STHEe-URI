entrada = float(input(''))
cem = entrada-(entrada%100)
saida1 = int(cem//100)
entrada = entrada-cem
cinquenta = entrada-(entrada%50)
saida2 = int(cinquenta//50)
entrada = entrada-cinquenta
vinte = entrada-(entrada%20)
saida3 = int(vinte//20)
entrada = entrada-vinte
dez = entrada-(entrada%10)
saida4 = int(dez//10)
entrada = entrada-dez
cinco = entrada-(entrada%5)
saida5 = int(cinco//5)
entrada = entrada-cinco
dois = entrada-(entrada%2)
saida6 = int(dois//2)

entrada1 = entrada-dois
umreal = entrada1-(entrada%1)
saida7 = int(umreal//1)
entrada1 = entrada1-umreal
cinquentacent = entrada1-(entrada%0.5)
saida8 = int(cinquentacent//0.5)
entrada1 = entrada1-cinquentacent
vintecent = entrada1-(entrada%0.25)
saida9 = int(vintecent//0.25)
entrada1 = entrada1-vintecent
dezcent = entrada1-(entrada%0.1)
saida10 = int(dezcent//0.1)
entrada1 = entrada1-dezcent
cincocent = entrada1-(entrada%0.05)
saida11 = int(cincocent//0.05)
entrada1 = entrada1-cincocent
saida12 = int(entrada1//0.01)
if entrada > 0.25:
saida10 = 0
saida11 = 0
saida12 = 0
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(saida1))
print('{} nota(s) de R$ 50.00'.format(saida2))
print('{} nota(s) de R$ 20.00'.format(saida3))
print('{} nota(s) de R$ 10.00'.format(saida4))
print('{} nota(s) de R$ 5.00'.format(saida5))
print('{} nota(s) de R$ 2.00'.format(saida6))

print('MOEDAS:')
print('{} moedas(s) de R$ 1.00'.format(saida7))
print('{} moedas(s) de R$ 0.50'.format(saida8))
print('{} moedas(s) de R$ 0.25'.format(saida9))
print('{} moedas(s) de R$ 0.10'.format(saida10))
print('{} moedas(s) de R$ 0.05'.format(saida11))
print('{} moedas(s) de R$ 0.01'.format(saida12))
