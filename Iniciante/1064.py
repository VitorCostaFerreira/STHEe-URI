n1 = float(input(''))
n2 = float(input(''))
n3 = float(input(''))
n4 = float(input(''))
n5 = float(input(''))
n6 = float(input(''))

positivos = 0
media = 0
entrada = [0,n1,0,n2,0,n3,0,n4,0,n5,0,n6]
entrada = entrada[1::2]

for i in range(0,6):
    if entrada[i] >= 0:
        positivos += 1
        media += entrada[i]
    else:
        i=i
print('{} valores positivos'.format(positivos))
print('{:0.1f}'.format(media/positivos))
