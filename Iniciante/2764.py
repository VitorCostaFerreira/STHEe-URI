X = list(map(str,input('').split('/')))
DD = X[0]
MM = X[1]
AA = X[2]

print('{}/{}/{}'.format(MM,DD,AA))
print('{}/{}/{}'.format(AA,MM,DD))
print('{}-{}-{}'.format(DD,MM,AA))
