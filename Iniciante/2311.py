def lista():
    total = 0
    GD = float(input(''))
    N = list(map(float,input('').split()))
    N.sort()
    N.remove(N[6])
    N.remove(N[0])
    for i in range(len(N)):
        total += N[i]
    return total*GD


X = int(input(''))
nome = list(range(X))
final = list(range(X))
for k in range(X):
    nome[k] = input('')
    final[k] = lista()
    print('{} {:0.2f}'.format(nome[k],final[k]))