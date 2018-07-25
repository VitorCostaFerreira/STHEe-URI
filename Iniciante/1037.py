N = float(input(''))

if 0 <= N <= 25:
    print('Intervalo [0,25]')
if 25.000000000001 <= N <= 50:
    print('Intervalo (25,50]')
if 50.000000000001 <= N <= 75:
    print('Intervalo (50,75]')
if 75.000000000001 <= N <= 100:
    print('Intervalo (75,100]')
if N < 0 or N > 100:
    print('Fora de intervalo')