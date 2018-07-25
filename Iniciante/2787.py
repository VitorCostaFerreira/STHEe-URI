L = int(input(''))
C = int(input(''))

if C == L:
    print('1')
else:
    if L%2 == 0:
        if C%2 == 0:
            print('1')
        elif C%2 != 0:
            print('0')
    elif L%2 != 0:
        if C%2 == 0:
            print('0')
        elif C%2 != 0:
            print('1')
