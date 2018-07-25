T = int(input(''))

for i in range(1,T+1):
    entrada = list(map(int, input('').split()))
    A = entrada[0]
    B = entrada[1]

    print('{}'.format(A+B))