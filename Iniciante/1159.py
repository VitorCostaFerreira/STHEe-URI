def teste():
    final = 0
    X = int(input(''))
    if X == 0:
        quit()
    else:
        for i in range(X,X+10):
            if i%2 == 0:
                final += i
            else:
                continue
        print(final)
try:
    while True:
        teste()
except:
    v = 0