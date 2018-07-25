X = int(input(''))
Y = int(input(''))
cont = resultado = 0
if Y > 0 and X > 0:
    if X > Y:
        for i in range(Y,X):
            if i%2 == 0:
                i=i
            else:
                resultado += i
    elif Y > X:
        for i in range(Y,X):
            if i%2 == 0:
                i=i
            else:
                resultado += i
else:
    if X > 0 and Y < 0:
        for i in range(Y+1,X):
            if i%2 == 0:
                i=i
            else:
                resultado += i
    elif Y > 0 and X < 0:
        for i in range(X+1,Y):
            if i%2 == 0:
                i=i
            else:
                resultado += i
    else:
        for i in range(X,Y):
            if i%2 == 0:
                i=i
            else:
                resultado += i
print(resultado)