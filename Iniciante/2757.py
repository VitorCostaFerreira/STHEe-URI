A = str(input(''))
B = str(input(''))
C = str(input(''))

a = 10-len(A)
b = 10-len(B)
c = 10-len(C)

finalA3 = ('{}'.format(A))+(' '*a)
finalB3 = ('{}'.format(B))+(' '*b)
finalC3 = ('{}'.format(C))+(' '*c)
finalA2 = ('0'*a)+('{}'.format(A))
finalB2 = ('0'*b)+('{}'.format(B))
finalC2 = ('0'*c)+('{}'.format(C))
finalA = (' '*a)+('{}'.format(A))
finalB = (' '*b)+('{}'.format(B))
finalC = (' '*c)+('{}'.format(C))

print('A = {}, B = {}, C = {}'.format(A,B,C))
print('A = {}, B = {}, C = {}'.format(finalA,finalB,finalC))
print('A = {}, B = {}, C = {}'.format(finalA2,finalB2,finalC2))
print('A = {}, B = {}, C = {}'.format(finalA3,finalB3,finalC3))

