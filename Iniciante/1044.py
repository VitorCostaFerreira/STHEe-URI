entrada = list(map(float, input('').split()))

A = entrada[0]
B = entrada[1]

if A%B == 0:
    print('Sao Multiplos')
elif B%A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')