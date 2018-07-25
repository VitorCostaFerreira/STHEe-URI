X = list(map(str,input('').split('.')))

inteiro = X[0]
decimal = X[1]

decimal = decimal.lstrip('0')

print('{}.{}'.format(decimal,inteiro))
