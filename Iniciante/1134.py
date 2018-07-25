Alcool = Gasolina = Diesel = 0
for i in range(0, 99999999):
    n = int(input(''))
    if n != (1,2,3,4):
        i=i
    if n == 1:
        Alcool += 1
    if n == 2:
        Gasolina += 1
    if n == 3:
        Diesel += 1
    if n == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(Alcool))
print('Gasolina: {}'.format(Gasolina))
print('Diesel: {}'.format(Diesel))