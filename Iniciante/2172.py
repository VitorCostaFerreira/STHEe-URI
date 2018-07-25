while True:
    X = list(map(int,input('').split()))
    if X[0] == X[1] == 0:
        break
    else:
        print(X[0]*X[1])