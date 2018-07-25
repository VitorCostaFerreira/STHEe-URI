N = list(range(20))

for i in range(20):
    N[i] = int(input(''))
N = N[::-1]
for j in range(20):
    print('N[{}] = {}'.format(j,N[j]))