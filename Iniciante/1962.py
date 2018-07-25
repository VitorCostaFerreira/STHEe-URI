N = int(input(''))

for i in range(0,N):
    X = int(input(''))
    final = X-2015
    if final >= 0:
        print('{} A.C.'.format(final+1))
    elif final < 0:
        final = -(final)
        print('{} D.C.'.format(final))
    #print(final)
