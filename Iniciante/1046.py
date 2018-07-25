entrada = list(map(int, input('').split()))
X = entrada[0]
Y = entrada[1]
cont = 0
if X > Y:
    Y += 24
    Total = -(X-Y)
    print('O JOGO DUROU {} HORA(S)'.format(Total))
elif X < Y:
    Total = Y-X
    print('O JOGO DUROU {} HORA(S)'.format(Total))
elif X == Y:
    print('O JOGO DUROU 24 HORA(S)')