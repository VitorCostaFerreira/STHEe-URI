X = [1,1,1,1,1,1,1,1,1,1]
for i in range(0,10):
    X[i] = int(input(''))
    if X[i] <= 0:
        X[i] = 1
    print('X[{}] = {}'.format(i,X[i]))