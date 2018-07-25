N = int(input(''))

total = 0

for i in range(0,N):
    entrada = list(map(int, input('').split()))
    X = entrada[0]
    Y = entrada[1]
    if X > Y:
        for j in range(Y+1, X):
           if j%2 != 0:
               total += j
           else:
               continue
        print('{}'.format(total))
        total = 0
    if Y > X:
        for a in range(X+1, Y):
            if a % 2 != 0:
                total += a
            else:
                continue
        print('{}'.format(total))
        total = 0
    elif Y == X:
        print('0')