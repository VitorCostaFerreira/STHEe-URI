n = int(input(''))
meses = 0
anos = n//365
dias = n%365
while dias > 30:
    dias -=30
    meses += 1
if dias >= 30:
    meses += 1
    dias = 0
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))