entrada = list(map(float, input('').split()))

X = entrada[0]
Y = entrada[1]

if X == Y == 0:
    print('Origem')
elif X == 0:
    print('Eixo Y')
elif Y == 0:
    print('Eixo X')
if X > 0:
    if Y > 0:
        print('Q1')
    elif Y < 0:
        print('Q4')
elif X < 0:
    if Y > 0:
        print('Q2')
    elif Y < 0:
        print('Q3')