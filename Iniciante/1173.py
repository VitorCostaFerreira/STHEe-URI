V = int(input(''))
N = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    if i == 0:
        N[i] = V
    else:
        N[i] = V*2
        V = V*2
    print('N[{}] = {}'.format(i,N[i]))