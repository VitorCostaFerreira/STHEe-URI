entrada = int(input(''))

DDD = [61,71,11,21,32,19,27,31]

if entrada in DDD:
    if entrada == 61:
        print('Brasilia')
    elif entrada == 71:
        print('Salvador')
    elif entrada == 11:
        print('Sao Paulo')
    elif entrada == 21:
        print('Rio de Janeiro')
    elif entrada == 32:
        print('Juiz de Fora')
    elif entrada == 19:
        print('Campinas')
    elif entrada == 27:
        print('Vitoria')
    elif entrada == 31:
        print('Belo Horizonte')
else:
    print('DDD nao cadastrado')