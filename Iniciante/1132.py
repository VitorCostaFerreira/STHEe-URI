X = int(input(''))
Y = int(input(''))
soma = 0
if X > Y:
    for i in range(Y, X+1):
        if i%13 == 0:
            i=i
        elif i%13 != 0:
            soma += i
    print(soma)
if Y > X:
    for i in range(X,Y+1):
        if i%13 == 0:
            i=i
        elif i%13 != 0:
            soma += i
    print(soma)
