import math
n = int(input(''))

horas = n//3600
'''(n - horas * 3600)/60'''
minutos = ((n - horas * 3600) / 60)
segundos = n%60

print('{}:{}:{}'.format(math.floor(horas),math.floor(minutos),segundos))
