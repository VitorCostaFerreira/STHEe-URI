X = list(map(int,input('').split()))
A = X[0]
B = X[1]
if B < 0:
    B = -(B)
    print(-((A) // (B)), end=' ')
    print((A) % (B))
else:
    print((A)//(B),end=' ')
    print((A)%(B))
