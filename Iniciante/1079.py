n = int(input(''))

peso1 = 2
peso2 = 3
peso3 = 5

for i in range(1,n+1):
    entrada = list(map(float, input('').split()))

    A = entrada[0]*peso1
    B = entrada[1]*peso2
    C = entrada[2]*peso3

    total = (A+B+C)/(peso1+peso2+peso3)
    print('{:0.1f}'.format(total))