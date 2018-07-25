try:
    for i in range(0,99999999999999):
        A = int(input(''))

        if A == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
except EOFError:
    quit()