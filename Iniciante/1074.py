X = int(input(''))
if X == 0:
    print('NULL')
else:
    for i in range(0, X):
        N = int(input(''))
        if N == 0:
            print('NULL')
        elif N%2 == 0:
            print('EVEN', end=' ')
            if N < 0:
                print('NEGATIVE')
            elif N > 0:
                print('POSITIVE')
        elif N%2 != 0:
            print('ODD', end=' ')
            if N < 0:
                print('NEGATIVE')
            elif N > 0:
                print('POSITIVE')