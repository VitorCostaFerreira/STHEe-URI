cont = idades = 0
while True:
    N = int(input(''))

    if N < 0:
        break
    else:
        cont += 1
        idades += N
        total = idades/cont
print('{:0.2f}'.format(total))