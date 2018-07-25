C = int(input(''))

for i in range(1, C+1):
    entrada = list(map(str, input('').split()))
    name = entrada[0]
    N = int(entrada[1])

    if name.upper() != 'THOR':
        print('N')
    else:
        print('Y')