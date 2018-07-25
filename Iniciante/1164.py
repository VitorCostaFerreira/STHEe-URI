def perfeito():
    X = int(input(''))
    for j in range(1,X+1):
        N = int(input(''))
        perfeito = 0
        for i in range(1,N):
            if N%i == 0:
                perfeito += i
        if perfeito == N:
            print('{} eh perfeito'.format(N))
        else:
            print('{} nao eh perfeito'.format(N))
perfeito()