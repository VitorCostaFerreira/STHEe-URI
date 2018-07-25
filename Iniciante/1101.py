total = 0
while True:
    entrada = list(map(int, input('').split()))
    M = entrada[0]
    N = entrada[1]
    if M == 0 or N == 0 or M < 0 or N < 0:
        break
    else:
        if M > N:
            for i in range(N, M+1):
                print(i,end=' ')
                total += i
            print('Sum={}'.format(total))
            total = 0
        elif N > M:
            for j in range(M, N+1):
                print(j,end=' ')
                total += j
            print('Sum={}'.format(total))
            total = 0
