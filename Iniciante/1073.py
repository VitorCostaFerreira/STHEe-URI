n = int(input(''))

for i in range(0,n+1):
    if i > 0:
        if i%2 == 0:
            print('{}^2 = {}'.format(i,i**2))
        else:
            i=i