n = int(input(''))
cont = 0
for i in range(1, 9999999999999999999, 4):
    print('{} {} {} PUM'.format(i, i+1, i+2))
    cont += 1
    if cont == n:
        break