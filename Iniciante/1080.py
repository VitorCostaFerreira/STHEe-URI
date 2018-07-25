for i in range(1, 101):

    n = int(input(''))
    if i == 1:
        maior = n
    else:
        if n > maior:
            maior = n
            posição = i
        elif n < maior:
            maior = maior
print('{}'.format(maior))
print('{}'.format(posição))
