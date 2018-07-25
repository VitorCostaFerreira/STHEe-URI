entrada = int(input(''))
print(entrada)
cem = entrada%100
#valor de cem = 76
outro = entrada-cem
teste = (outro//100)
entrada = cem
cinq = entrada%50
#valor de cinq = 26
outro1 = entrada-cinq
teste1 = (outro1//50)
entrada = cinq
vinte = entrada%20
#valor de vinte = 6
outro2 = entrada-vinte
teste2 = (outro2//20)
entrada = vinte
dez = entrada%10
#valor de vinte = 6
outro3 = entrada-dez
teste3 = (outro3//10)
entrada = dez
cin = entrada%5
#valor de vinte = 1
outro4 = entrada-cin
teste4 = (outro4//5)
entrada = cin
dois = entrada%2
#valor de vinte = 1
outro5 = entrada-dois
teste5 = (outro5//2)
entrada = dois
um = entrada%1
#valor de vinte = 0
outro6 = entrada-um
teste6 = (outro6//1)

print('{} nota(s) de R$ 100,00'.format(teste))
print('{} nota(s) de R$ 50,00'.format(teste1))
print('{} nota(s) de R$ 20,00'.format(teste2))
print('{} nota(s) de R$ 10,00'.format(teste3))
print('{} nota(s) de R$ 5,00'.format(teste4))
print('{} nota(s) de R$ 2,00'.format(teste5))
print('{} nota(s) de R$ 1,00'.format(teste6))