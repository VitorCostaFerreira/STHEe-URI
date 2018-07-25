while True:
    n1 = float(input(''))
    while 0<n1<=10:
        n2 = float(input(''))
        if 0<n2<=10:
            total = (n1+n2)/2
            print('media = {:0.2f}'.format(total))
            quit()
        else:
            print('nota invalida')
    else:
        print('nota invalida')